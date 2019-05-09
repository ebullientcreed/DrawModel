# Thekkumpat,Navaneeth. 
# nxt6413
# 2019-05-02

#---------#---------#---------#---------#---------#--------#
def constructTransform( w, v, width, height ) :
    ##################################################
    # Put your Python code for computing fx, fy, gx, gy, sx, sy,
    # ax, and ay here.
    #
    # Return ax, ay, sx, and sy as a tuple.
    ##################################################
    wxmin=w[0]
    wymin=w[1]
    vxmin=v[0]
    vymin=v[1]
    wxmax=w[2]
    wymax=w[3]
    vxmax=v[2]
    vymax=v[3]
    fx=-wxmin
    fy=-wymin
    gx=width*vxmin
    gy=height*vymin
    sx=(width*(vxmax-vxmin))/(wxmax-wxmin)
    sy=(height*(vymax-vymin))/(wymax-wymin)
    ax=(fx*sx)+gx;
    ay=(fy*sy)+gy;
    return (ax,ay,sx,sy)    


#---------#---------#---------#---------#---------#--------#
def _main() :
  w      = ( -1.0, -2.0, 4.0, 5.0 )
  v      = ( 0.15, 0.15, 0.85, 0.85 )
  width  = 500
  height = 400

  values = constructTransform( w, v, width, height )
  ax, ay, sx, sy = values

  print( f'Values          : {values}' )
  print( f'Test transform  : ax {ax}, ay {ay}, sx {sx}, sy {sy}' )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
