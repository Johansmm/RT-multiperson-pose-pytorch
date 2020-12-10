

#from matplotlib import colors


def Heatmapgraph(img,heatmap,id_heat,plt,np):


  cmap='rainbow'
  interpolation='bicubic'
  alpha=.6

  fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(15,15))
  images = []
  aux =0

  plt.imshow(img, alpha=1) # for image
  xmin, xmax = plt.xlim()
  ymin, ymax = plt.ylim()
  
  # Generate data with a range that varies from one plot to the next.
  ImagMap=heatmap[:,:,id_heat]
  axs.imshow(img, alpha=1) 
  axs.imshow(ImagMap, cmap=cmap, interpolation=interpolation,alpha=alpha,extent=(xmin,xmax,ymin,ymax))
  plt.grid(b=False)
  plt.axis('off')
  plt.show()

def graphPAF(img,paf,id_paf,plt,np):
  
  out_paf = np.zeros([paf.shape[2], img.shape[0], img.shape[1]])

  for h in range(paf.shape[2]):
    out_paf[h] = cv2.resize(paf[:,:,h], (img.shape[1], img.shape[0]))
  X, Y = np.meshgrid(np.arange(0, img.shape[1], 1) , np.arange(0, img.shape[0], 1))

  fig, ax = plt.subplots(nrows= 1, ncols = 1, figsize = (15,10), sharex=True, sharey=True)
  colors = np.random.randint(0, 255, size = (2*3,3), dtype = "uint8") / 255.0

  ax.imshow(img, alpha = 0.8)
  ax.quiver(X, Y, out_paf[2*id_paf], out_paf[2*id_paf + 1], minlength=0, alpha = 0.5, color = 'red')
  ax.set_xticklabels([]); ax.set_yticklabels([])
  ax.set_xticks([]); ax.set_yticks([])
  fig.show()

def graphGridHeatmap(img,Grahp,heatmap,plt,colors):
  Nr = 2
  Nc = 3
  
  cmap='rainbow'
  interpolation='bicubic'
  alpha=.6

  fig, axs = plt.subplots(Nr, Nc,figsize=(15,15))
  fig.suptitle('Part Confidence Maps')

  images = []
  aux =0

  plt.imshow(img, alpha=1) # for image
  xmin, xmax = plt.xlim()
  ymin, ymax = plt.ylim()
  for i in range(Nr):
      for j in range(Nc):
          # Generate data with a range that varies from one plot to the next.
          ImagMap=heatmap[:,:,Grahp[aux]]
          axs[i, j].imshow(img, alpha=1) 
          images.append(axs[i, j].imshow(ImagMap, cmap=cmap, interpolation=interpolation,alpha=alpha,extent=(xmin,xmax,ymin,ymax)))
          axs[i, j].label_outer()
          axs[i, j].grid(b=False)
          axs[i, j].axis('off')
          aux+=1

  # Find the min and max of all colors for use in setting the color scale.
  vmin = min(image.get_array().min() for image in images)
  vmax = max(image.get_array().max() for image in images)
  norm = colors.Normalize(vmin=vmin, vmax=vmax)
  for im in images:
      im.set_norm(norm)

  fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)

  plt.grid(b=False)
  plt.axis('off')
  plt.show()

def graphGridPaf(img,paf,paf_view,plt,np,cv2):

  out_paf = np.zeros([paf.shape[2], img.shape[0], img.shape[1]])

  for h in range(paf.shape[2]):
    out_paf[h] = cv2.resize(paf[:,:,h], (img.shape[1], img.shape[0]))
  X, Y = np.meshgrid(np.arange(0, img.shape[1], 1) , np.arange(0, img.shape[0], 1))

  fig, axs = plt.subplots(nrows= 2, ncols = 3, figsize = (15,10), sharex=True, sharey=True)
  
  colors = np.random.randint(0, 255, size = (2*3,3), dtype = "uint8") / 255.0
  for i,ax in enumerate(axs.flatten()):
    ax.imshow(img, alpha = 0.8)
    ax.quiver(X, Y, out_paf[2*paf_view[i]], out_paf[2*paf_view[i] + 1], 
              minlength=0, alpha = 0.5, color = colors[i])
    ax.set_xticklabels([]); ax.set_yticklabels([])
    ax.set_xticks([]); ax.set_yticks([]); ax.axis("on")

  fig.subplots_adjust(wspace=0.0,hspace=0.0)
  fig.suptitle("Part Affinity Fields", fontsize=16)
  fig.show()