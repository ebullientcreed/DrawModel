# Thekkumpat,Navaneeth. 
# nxt6413
# 2019-04-24

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2019 Spring semester.

#----------------------------------------------------------------------
import CohenSutherland as cs
import beizer as bz
import numpy
class cl_world :
  def __init__( self, objects = [], canvases = [] ) :
    self.canvases = canvases
    self.bzr=bz.beizer_C()

  def add_canvas( self, canvas ) :
    self.canvases.append( canvas )
    canvas.world = self

  def reset( self ) :
    for canvas in self.canvases :
      canvas.delete( 'all' )

  def calculate_each_point(self, canvas,resolution,pointList,doClip,viewValues):

    if doClip==0:
      for row in range(0,resolution-1):
        rowStart=row*resolution
        for col in range(0,resolution-1):
          here=rowStart+col
          there=here+resolution        
          firstA=(pointList[here][0],pointList[here][1],pointList[there][0],pointList[there][1])
          secondA=(pointList[there][0],pointList[there][1],pointList[there+1][0],pointList[there+1][1])
          thirdA=(pointList[there+1][0],pointList[there+1][1],pointList[here][0],pointList[here][1])        
          canvas.create_line(firstA, secondA )
          canvas.create_line(secondA,thirdA )
          canvas.create_line(thirdA, firstA )
          firstB=(pointList[there+1][0],pointList[there+1][1],pointList[here+1][0],pointList[here+1][1])
          secondB=(pointList[here+1][0],pointList[here+1][1],pointList[here][0],pointList[here][1])
          thirdB=(pointList[here][0],pointList[here][1],pointList[there+1][0],pointList[there+1][1])                 
          canvas.create_line(firstB, secondB )
          canvas.create_line(secondB,thirdB )
          canvas.create_line(thirdB, firstB )
    else:
      for row in range(0,resolution-1):
        rowStart=row*resolution
        for col in range(0,resolution-1):
          here=rowStart+col
          there=here+resolution        
          firstA=(pointList[here][0],pointList[here][1],pointList[there][0],pointList[there][1])
          secondA=(pointList[there][0],pointList[there][1],pointList[there+1][0],pointList[there+1][1])
          thirdA=(pointList[there+1][0],pointList[there+1][1],pointList[here][0],pointList[here][1])        
          firstB=(pointList[there+1][0],pointList[there+1][1],pointList[here+1][0],pointList[here+1][1])
          secondB=(pointList[here+1][0],pointList[here+1][1],pointList[here][0],pointList[here][1])
          thirdB=(pointList[here][0],pointList[here][1],pointList[there+1][0],pointList[there+1][1])
          (dodraw1,x1,y1,x2,y2)=cs.clipLine(firstA[0],firstA[1],secondA[0],secondA[1],viewValues)
          if dodraw1 == True :
            canvas.create_line(x1,y1,x2,y2)
          (dodraw2,x3,y3,x4,y4)=cs.clipLine(secondA[0],secondA[1],thirdA[0],thirdA[1],viewValues)
          if dodraw2 == True :
             canvas.create_line(x3,y3,x4,y4)
          (dodraw3,x5,y5,x6,y6)=cs.clipLine(thirdA[0],thirdA[1],firstA[0],firstA[1],viewValues)
          if dodraw3 == True :
            canvas.create_line(x5,y5,x6,y6 )
          (dodraw1,x7,y7,x8,y8)=cs.clipLine(firstB[0],firstB[1],secondB[0],secondB[1],viewValues)
          if dodraw1 == True :
            canvas.create_line(x7,y7,x8,y8)
          (dodraw2,x9,y9,x10,y10)=cs.clipLine(secondB[0],secondB[1],thirdB[0],thirdB[1],viewValues)
          if dodraw2 == True :
             canvas.create_line(x9,y9,x10,y10)
          (dodraw3,x11,y11,x12,y12)=cs.clipLine(thirdB[0],thirdB[1],firstB[0],firstB[1],viewValues)
          if dodraw3 == True :
            canvas.create_line(x11,y11,x12,y12 )                 
          

  def create_graphic_objects( self, canvas,mdl,doClip, doPerspective,doEuler,resolution  ) :
    xminm=float(canvas.cget( 'width' ))*mdl.getViewport()[0]
    xmaxm=float(canvas.cget( 'width' ))*mdl.getViewport()[2]
    yminm=float(canvas.cget( 'height' ))*mdl.getViewport()[1]    
    ymaxm=float(canvas.cget( 'height' ))*mdl.getViewport()[3]
    canvas.create_rectangle(xminm,yminm,xmaxm,ymaxm)
    vertices=mdl.getVertices()
    faces=mdl.getFaces()
    patches=mdl.getPatches() 
      
    viewValues=[]
    viewValues=[xminm,yminm,xmaxm,ymaxm]
    
    if doClip==0:
      
      
      if len(mdl.getFaces())==0:   
        for patch in patches:
          ctl=[]
          pointList=[]
          for p in patch :
            p1 = mdl.getTransformedVertex(vertices[p],doPerspective,doEuler)
            ctl.append(p1)              
          pointList=self.bzr.resolveBezierPatch(resolution,ctl)
          self.calculate_each_point(canvas,resolution,pointList,doClip,viewValues)
      for i in range(0, len(mdl.getFaces())):
        first = mdl.getTransformedVertex(vertices[faces[i][0]],doPerspective,doEuler)
        second= mdl.getTransformedVertex(vertices[faces[i][1]],doPerspective,doEuler)
        third= mdl.getTransformedVertex(vertices[faces[i][2]],doPerspective,doEuler)
        canvas.create_line(first[0],first[1], second[0],second[1] )
        canvas.create_line(second[0],second[1],third[0],third[1] )
        canvas.create_line(third[0],third[1], first[0],first[1] )    

    else:
      for i in range(0, len(mdl.getFaces())):
        first = mdl.getTransformedVertex(vertices[faces[i][0]],doPerspective,doEuler)
        second= mdl.getTransformedVertex(vertices[faces[i][1]],doPerspective,doEuler)
        third= mdl.getTransformedVertex(vertices[faces[i][2]],doPerspective,doEuler)
        (dodraw1,x1,y1,x2,y2)=cs.clipLine(first[0],first[1],second[0],second[1],viewValues)
        if dodraw1 == True :
        	canvas.create_line(x1,y1,x2,y2)
        (dodraw2,x3,y3,x4,y4)=cs.clipLine(second[0],second[1],third[0],third[1],viewValues)
        if dodraw2 == True :
        	 canvas.create_line(x3,y3,x4,y4)
        (dodraw3,x5,y5,x6,y6)=cs.clipLine(third[0],third[1],first[0],first[1],viewValues)
        if dodraw3 == True :
        	canvas.create_line(x5,y5,x6,y6 )
      
      if len(mdl.getFaces())==0:  
        for patch in patches:
          ctl=[]
          pointList=[]
          for p in patch :
            p1 = mdl.getTransformedVertex(vertices[p],doPerspective,doEuler)              
            ctl.append(p1)                     
          pointList=self.bzr.resolveBezierPatch(resolution,ctl)
          self.calculate_each_point(canvas,resolution,pointList,doClip,viewValues)      

    # 2. Create a line that goes from the lower left to
    #    the upper right of the canvas.
    #canvas.create_line(
     # canvas.cget( 'width' ), 0, 0, canvas.cget( 'height' ) )

    # 3. Create an oval that is centered on the canvas
    #    and is 50% as wide and 50% as high as the canvas.
    #canvas.create_oval(
     # int( 0.25 * int( canvas.cget( 'width' ) ) ),
     # int( 0.25 * int( canvas.cget( 'height' ) ) ),
     # int( 0.75 * int( canvas.cget( 'width' ) ) ),
     # int( 0.75 * int( canvas.cget( 'height' ) ) ) )

#----------------------------------------------------------------------
