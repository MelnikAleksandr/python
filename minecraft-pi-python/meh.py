import mcpi.minecraft as minecraft
import mcpi.block as block
 
mc = minecraft.Minecraft.create()
 
mc.postToChat("This Is Meh")

def CreateLandscape(moatwidth,moatdepth,islandwidth):
  # Set upper half to air
  mc.setBlocks(-128,1,-128,128,128,128,block.AIR)
  # Set lower half of world to dirt with a layer of grass
  mc.setBlocks(-128,-1,-128,128,-128,128,block.DIRT)
  mc.setBlocks(-128,0,-128,128,0,128,block.GRASS)
  
  
  
  print("Create ground")
CreateLandscape(33,10,23)  
