# Thekkumpat,Navaneeth. 
# nxt6413
# 2019-05-02
#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2019 Spring semester.

#----------------------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import ModelData 
import constructTransform
import math
#----------------------------------------------------------------------
class cl_widgets :
  def __init__( self, ob_root_window, ob_world = [] ) :
    self.ob_root_window = ob_root_window
    self.ob_world = ob_world

    self.checkVar=tk.BooleanVar();
    self.perVar=tk.BooleanVar();
    self.eulVar=tk.BooleanVar();

    self.menu = cl_menu( self )

    self.toolbar = cl_toolbar( self )

    self.statusBar_frame = cl_statusBar_frame( self.ob_root_window )
    self.statusBar_frame.pack( side = tk.BOTTOM, fill = tk.X )
    self.statusBar_frame.set( 'This is the status bar' )

    self.ob_canvas_frame = cl_canvas_frame( self )
    self.ob_world.add_canvas( self.ob_canvas_frame.canvas )

#----------------------------------------------------------------------
class cl_canvas_frame :
  def __init__( self, master ) :
    self.master = master
    self.canvas = tk.Canvas(
      master.ob_root_window, width=1, height=1, bg='turquoise' )

    self.canvas.pack( expand=tk.YES, fill=tk.BOTH )
    self.canvas.bind( '<Configure>',       self.canvas_resized_callback )
    self.canvas.bind( '<Key>',             self.key_callback )

    self.canvas.bind( '<ButtonPress-1>',   lambda e : self.btn_callback( 'LMB', 'press', e ) )
    self.canvas.bind( '<ButtonRelease-1>', lambda e : self.btn_callback( 'LMB', 'release', e ) )
    self.canvas.bind( '<B1-Motion>',       lambda e : self.btn_callback( 'LMB', 'motion', e ) )
    self.canvas.bind( '<ButtonPress-2>',   lambda e : self.btn_callback( 'MMB', 'press', e ) )
    self.canvas.bind( '<ButtonRelease-2>', lambda e : self.btn_callback( 'MMB', 'release', e ) )
    self.canvas.bind( '<B2-Motion>',       lambda e : self.btn_callback( 'MMB', 'motion', e ) )
    self.canvas.bind( '<ButtonPress-3>',   lambda e : self.btn_callback( 'RMB', 'press', e ) )
    self.canvas.bind( '<ButtonRelease-3>', lambda e : self.btn_callback( 'RMB', 'release', e ) )
    self.canvas.bind( '<B3-Motion>',       lambda e : self.btn_callback( 'RMB', 'motion', e ) )

    self.canvas.bind( '<Up>',              lambda e : self.arrow_callback( 'Up', False, e ) )
    self.canvas.bind( '<Down>',            lambda e : self.arrow_callback( 'Down', False, e ) )
    self.canvas.bind( '<Right>',           lambda e : self.arrow_callback( 'Right', False, e ) )
    self.canvas.bind( '<Left>',            lambda e : self.arrow_callback( 'Left', False, e ) )
    self.canvas.bind( '<Shift-Up>',        lambda e : self.arrow_callback( 'Up', True, e ) )
    self.canvas.bind( '<Shift-Down>',      lambda e : self.arrow_callback( 'Down', True, e ) )
    self.canvas.bind( '<Shift-Right>',     lambda e : self.arrow_callback( 'Right', True, e ) )
    self.canvas.bind( '<Shift-Left>',      lambda e : self.arrow_callback( 'Left', True, e ) )

  def arrow_callback( self, arrow, shift, event ) :
    shiftValue = 'Shift-' if shift else ''
    self.master.statusBar_frame.set( f'{shiftValue}{arrow} arrow pressed.' )

  def btn_callback( self, btn, action, event ) :
    if action == 'press' :
      self.master.statusBar_frame.set( f'{btn} pressed. ({event.x}, {event.y})' )
      self.x = event.x
      self.y = event.y
      self.canvas.focus_set()

    elif action == 'release' :
      self.master.statusBar_frame.set( f'{btn} released. ({event.x}, {event.y})' )
      self.x = None
      self.y = None

    elif action == 'motion' :
      self.master.statusBar_frame.set( f'{btn} dragged. ({event.x}, {event.y})' )
      self.x = event.x
      self.y = event.y

    else :
      self.master.statusBar_frame.set( f'Unknown {btn} action {action}.' )

  def key_callback( self, event ) :
    msg = f'{event.char!r} ({ord( event.char )})' \
      if len( event.char ) > 0 else '<non-printing char>'

    self.master.statusBar_frame.set(
      f'{msg} pressed at ({event.x},{event.y})' )

  def canvas_resized_callback( self, event ) :
    self.canvas.config( width = event.width-4, height = event.height-4 )

    self.master.statusBar_frame.pack( side = tk.BOTTOM, fill = tk.X )
    self.master.statusBar_frame.set(
      f'Canvas width, height ({self.canvas.cget( "width" )}, ' +
      f'{self.canvas.cget( "height" )})' )

    self.canvas.pack()

#----------------------------------------------------------------------
class cl_statusBar_frame( tk.Frame ) :
  def __init__( self, master ) :
    tk.Frame.__init__( self, master )
    self.label = tk.Label( self, bd = 1, relief = tk.SUNKEN, anchor = tk.W )
    self.label.pack( fill = tk.X )

  def set( self, formatStr, *args ) :
  	#print(formatStr)
    self.label.config( text = 'nxt6413: '+formatStr % args )
    self.label.update_idletasks()

  def clear( self ) :
    self.label.config( text='' )
    self.label.update_idletasks()

#----------------------------------------------------------------------
class cl_menu :
  def __init__( self, master ) :
    self.master = master
    self.menu = tk.Menu( master.ob_root_window )
    master.ob_root_window.config( menu = self.menu )
     
    dummy = tk.Menu( self.menu )
    self.menu.add_cascade( label = 'File', menu = dummy )
    dummy.add_command( label = 'New', command = lambda : self.menu_callback( 'file>new' ) )
    dummy.add_command( label = 'Open...', command = lambda : self.menu_callback( 'file>open' ) )
    dummy.add_separator()
    dummy.add_command( label = 'Exit', command = lambda : self.menu_callback( 'file>exit' ) )

   
    dummy = tk.Menu( self.menu )
    self.menu.add_cascade( label = 'Settings', menu = dummy )
    dummy.add_checkbutton( label = 'Clip',variable = self.master.checkVar, command = lambda : self.menu_callback( 'settings>Clip' ) ) 
    dummy.add_checkbutton( label = 'Persepective',variable = self.master.perVar, command = lambda : self.menu_callback( 'settings>Perspective' ) ) 
    dummy.add_checkbutton( label = 'Euler',variable = self.master.eulVar, command = lambda : self.menu_callback( 'settings>Euler' ) ) 

    dummy = tk.Menu( self.menu )
    self.menu.add_cascade( label = 'Help', menu = dummy )
    dummy.add_command( label = 'About...', command = lambda : self.menu_callback( 'help>about' ) )

  def menu_callback( self, which = None ) :
    item = 'menu' if which is None else which
    self.master.statusBar_frame.set( f'{item!r} callback' )

#----------------------------------------------------------------------
class cl_toolbar :
  def __init__( self, master ) :
    self.master = master
    self.toolbar = tk.Frame( master.ob_root_window )
    # intializing the mdl
    self.mdl=None
    self.f=0
    self.phi=0
    self.psi=0
    self.theta=0
    self.res=0

    dummy = tk.Button( self.toolbar, text = 'Resolution', width = 16, command = self.resolution_callback)
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'Distance', width = 16, command = self.distance_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'φ', width = 2, command = lambda : self.angle_callback('φ') )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )
    dummy = tk.Button( self.toolbar, text = 'θ', width = 2, command = lambda : self.angle_callback('θ') )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )
    dummy = tk.Button( self.toolbar, text = 'ψ', width = 2, command = lambda : self.angle_callback('ψ') )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    
    dummy = tk.Button( self.toolbar, text = 'Reset', width = 16, command = self.reset_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'Load', width = 16, command = self.load_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'Draw', width = 16, command = self.draw_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    self.toolbar.pack( side = tk.TOP, fill = tk.X )

  def distance_callback( self ) : 
    temp = simpledialog.askfloat( "Title", "Prompt?",initialvalue = self.f, minvalue = 0 )
    if temp is None:
      self.master.statusBar_frame.set( 'Canceled' )
    else:
      self.f=temp
      self.master.statusBar_frame.set( f'Entered distance{self.f}' )

  def angle_callback( self, which ) : 
  	if which=='φ':
  		temp1= simpledialog.askfloat( "Title", "Prompt?",initialvalue = self.phi, minvalue = 0 )
  		if temp1 is None:
  			self.master.statusBar_frame.set('Canceled')
  		else:  			
  			self.phi=temp1
  	if which=='θ':
  		temp2 = simpledialog.askfloat( "Title", "Prompt?",initialvalue = self.theta, minvalue = 0 )
  		if temp2 is None:
  			self.master.statusBar_frame.set('Canceled')
  		else:  			
  			self.theta=temp2
  	if which=='ψ':
  		temp3 = simpledialog.askfloat( "Title", "Prompt?",initialvalue = self.psi, minvalue = 0 )
  		if temp3 is None:
  			self.master.statusBar_frame.set('Canceled')
  		else:  			
  			self.psi=temp3				

  def resolution_callback( self ):
    tempr= simpledialog.askinteger( "Title", "Prompt?",initialvalue = self.res, minvalue = 4 )
    if tempr is None:
      self.master.statusBar_frame.set('Canceled')
    else:
      self.res=tempr

  def reset_callback( self ) :
    self.master.ob_world.reset()
    self.master.statusBar_frame.set( 'Reset callback' )

  def load_callback( self ) :
    fName = tk.filedialog.askopenfilename( filetypes = [ ( "allfiles", "*" ) ] )
    if len(fName)==0 :
      self.master.statusBar_frame.set( 'This is the canceled/loaded' )
    else:
      self.mdl=ModelData.ModelData(str(fName))
      self.master.statusBar_frame.set( 'Load callback' )

  def draw_callback( self ) :
    if self.mdl is None:
      self.master.statusBar_frame.set( 'Mesh load error' )
    else:
      wid=int(self.master.ob_canvas_frame.canvas.cget( 'width' ))  
      height=int(self.master.ob_canvas_frame.canvas.cget( 'height' ))
      window=self.mdl.getWindow()
      viewport=self.mdl.getViewport()
      transformValues = constructTransform.constructTransform( window, viewport, wid, height )
      
      self.mdl.specifyEuler(self.phi,self.theta,self.psi)
      
      self.mdl.specifyTransform(transformValues[0],transformValues[1],transformValues[2],transformValues[3],self.f)
      self.master.ob_world.create_graphic_objects( self.master.ob_canvas_frame.canvas,self.mdl,self.master.checkVar.get(),self.master.perVar.get(),self.master.eulVar.get(),self.res)
      
      self.master.statusBar_frame.set(f'resolution{self.res} ,distance {self.f},  φ{self.phi}°  θ{self.theta}°  ψ{self.psi}°')
      
      	
#----------------------------------------------------------------------
