# Thekkumpat,Navaneeth. 
# nxt6413
# 2019-05-02

import sys
import math

class ModelData() :
  def __init__( self, inputFile = None ) :
    self.m_Vertices = []
    self.m_Faces    = []
    self.m_Window   = []
    self.m_Viewport = []
    self.m_Patches  = []

    self.distance   = 0
    self.m_minX     = float( '+inf' )
    self.m_maxX     = float( '-inf' )
    self.m_minY     = float( '+inf' )
    self.m_maxY     = float( '-inf' )
    self.m_minZ     = float( '+inf' )
    self.m_maxZ     = float( '-inf' )

    self.m_r00=0
    self.m_r01=0
    self.m_r02=0
    self.m_r10=0
    self.m_r11=0
    self.m_r12=0
    self.m_r20=0
    self.m_r21=0
    self.m_r22=0
    self.m_ex=0
    self.m_ey=0
    self.m_ez=0

    if inputFile is not None :
      # File name was given.  Read the data from the file.
      self.loadFile( inputFile )

  def loadFile( self, inputFile ) :
    with open( inputFile, 'r' ) as fp :
      lines = fp.read().replace('\r', '' ).split( '\n' )
    wcount=0
    scount=0
    for ( index, line ) in enumerate( lines, start = 1 ) :
      line = line.strip()
      if ( line == '' or line[ 0 ] == '#' ) :
        continue

      if ( line[ 0 ] == 'v' ) :
        try :
          ( _, x, y, z ) = line.split()
          x = float( x )
          y = float( y )
          z = float( z )

          self.m_minX = min( self.m_minX, x )
          self.m_maxX = max( self.m_maxX, x )
          self.m_minY = min( self.m_minY, y )
          self.m_maxY = max( self.m_maxY, y )
          self.m_minZ = min( self.m_minZ, z )
          self.m_maxZ = max( self.m_maxZ, z )

          self.m_Vertices.append( ( x, y, z ) )

        except :
          print( 'Line %d is a malformed vertex spec.' % index )

      elif ( line[ 0 ] == 'f' ) :
        try :
          ( _, v1, v2, v3 ) = line.split()
          v1 = int( v1 )-1
          v2 = int( v2 )-1
          v3 = int( v3 )-1
          self.m_Faces.append( ( v1, v2, v3 ) )

        except :
          print( 'Line %d is a malformed face spec.' % index )

      elif ( line[ 0 ] == 'p' ) :
        try :
          ( _, p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16) = line.split()
          p1 = int( p1 )-1
          p2 = int( p2 )-1
          p3 = int( p3 )-1
          p4 = int( p4 )-1
          p5 = int( p5 )-1
          p6 = int( p6 )-1
          p7 = int( p7 )-1
          p8 = int( p8 )-1
          p9 = int( p9 )-1
          p10 = int( p10 )-1
          p11 = int( p11 )-1
          p12 = int( p12 )-1
          p13 = int( p13 )-1
          p14 = int( p14 )-1
          p15 = int( p15 )-1
          p16 = int( p16 )-1

          self.m_Patches.append(  (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16)  )

        except :
          print( 'Line %d is a malformed patches spec.' % index )    

      elif ( line[ 0 ] == 'w' ) :
        	try:
	      	  ( _, w1, w2, w3, w4 ) = line.split()
	      	  w1 = float( w1 )
	      	  w2 = float( w2 )
	      	  w3 = float( w3 )
	      	  w4 = float( w4 )
	      	  self.m_Window= ( w1, w2, w3, w4 ) 
	      	  wcount+=1
	      	  if(wcount>1):
	      	  	print( 'Line %d is a duplicate window spec.' % index )

        	except:
	            print( 'Line %d is a malformed window spec.' % index )

      elif ( line[ 0 ] == 's' ) :
       	try :
          ( _, s1, s2, s3, s4 ) = line.split()
          s1 = float( s1 )
          s2 = float( s2 )
          s3 = float( s3 )
          s4 = float( s4 )
          self.m_Viewport= ( s1, s2, s3,s4 ) 
          scount+=1
          if(scount>1):
            print( 'Line %d is a duplicate viewport spec.' % index )
        except :
          
       	  print( 'Line %d is a malformed viewport spec.' % index )
     
       		
      ##################################################
      # Put your Python code for reading and processing the w and
      # s lines here.
      #
      # The w line has four floats after the w.  Convert the
      # string representation to float and save the four values
      # as a tuple in self.m_Window.  Report any conversion errors
      # or if there are not exactly four floats following the w.
      #
      # The s line has four floats after the s.  Convert the
      # string representation to float and save the four values
      # as a tuple in self.m_Viewport.  Report any conversion
      # errors or if there are not exactly four floats following
      # the s.  (It's OK for an int to be given instead of a
      # float.  That is, for example, 1 is OK instead of 1.0.)
      #
      # Finally, there should be no more than one w line and no
      # more than one s line in the model file.  If there is more
      # than one of either kind of line, each such line should be
      # reported as a duplicate.
      #
      # If there are duplicate w and/or s lines, remember the
      # values from the _last_ valid such line.
      ##################################################

      else :
          print( 'Line %d \'%s\' is unrecognized.' % ( index, line ) )

  def getCenter( self ) :
    return (
      ( self.m_minX + self.m_maxX ) / 2.0,
      ( self.m_minY + self.m_maxY ) / 2.0,
      ( self.m_minZ + self.m_maxZ ) / 2.0 )
  
  def specifyTransform(self, ax, ay, sx, sy,distance):
    self.ax=ax
    self.ay=ay
    self.sx=sx
    self.sy=sy
    self.distance=distance
    
  def getTransformedVertex(self, vNum, doPerspective,doEuler ):
      xe=vNum[0]
      ye=vNum[1]
      ze=vNum[2]
      if doEuler:
        xe=(self.m_r00*vNum[0])+(self.m_r01*vNum[1])+(self.m_r02*vNum[2])+self.m_ex
        ye=(self.m_r10*vNum[0])+(self.m_r11*vNum[1])+(self.m_r12*vNum[2])+self.m_ey
        ze=(self.m_r20*vNum[0])+(self.m_r21*vNum[1])+(self.m_r22*vNum[2])+self.m_ez

      if doPerspective:
        if self.distance>ze and self.distance!=0:
          sf=1-(ze/self.distance)
          xprime=(self.sx*(xe/sf))+self.ax
          yprime=(self.sy*(ye/sf))+self.ay
        else:
          xprime=self.ax
          yprime=self.ay
      else :
        xprime=(self.sx*xe)+self.ax
        yprime=(self.sy*ye)+self.ay

      return (xprime,yprime,0.0)
  def specifyEuler(self, phi,theta,psi): 
  	  phi = math.radians(phi)
  	  theta = math.radians(theta)
  	  psi = math.radians(psi)
  	  cphi,sphi=(math.cos(phi),math.sin(phi))
  	  ctheta,stheta=(math.cos(theta),math.sin(theta))
  	  cpsi,spsi=(math.cos(psi),math.sin(psi))
  	  self.m_r00=cpsi*ctheta
  	  self.m_r01=-ctheta*spsi
  	  self.m_r02=stheta
  	  self.m_r10=(cphi*spsi)+(cpsi*sphi*stheta)
  	  self.m_r11=(cphi*cpsi)-(sphi*spsi*stheta)
  	  self.m_r12=-(ctheta*sphi)
  	  self.m_r20=-(cphi*cpsi*stheta)+(sphi*spsi)
  	  self.m_r21=(cphi*spsi*stheta)+(cpsi*sphi)
  	  self.m_r22=cphi*ctheta
  	  tx,ty,tz=self.getCenter()
  	  self.m_ex=-(self.m_r00*tx)-(self.m_r01*ty)-(self.m_r02*tz)+tx
  	  self.m_ey=-(self.m_r10*tx)-(self.m_r11*ty)-(self.m_r12*tz)+ty
  	  self.m_ez=-(self.m_r20*tx)-(self.m_r21*ty)-(self.m_r22*tz)+tz

  def getFaces( self )    : return self.m_Faces
  def getVertices( self ) : return self.m_Vertices
  def getViewport( self ) : return self.m_Viewport
  def getWindow( self )   : return self.m_Window
  def getPatches( self )  : return self.m_Patches

#---------#---------#---------#---------#---------#--------#
def _main() :
  # Get the file name to load.
  fName = sys.argv[1]

  # Create a ModelData object to hold the model data from
  # the supplied file name.
  model = ModelData( fName )

  # Now that it's loaded, print out a few statistics about
  # the model data that we just loaded.
  print( f'{fName}: {len( model.getVertices() )} vert%s, {len( model.getFaces() )} face%s' % (
    'ex' if len( model.getVertices() ) == 1 else 'ices',
    '' if len( model.getFaces() ) == 1 else 's' ))

  print( 'First 3 vertices:' )
  for v in model.getVertices()[0:3] :
    print( f'     {v}' )

  print( 'First 3 faces:' )
  for f in model.getFaces()[0:3] :
    print( f'     {f}' )

  print( f'Window line    : {model.getWindow()}' )
  print( f'Viewport line  : {model.getViewport()}' )

  print( f'Center         : {model.getCenter()}' )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
