class Properties:
  def __init__(self, tk, root):
    self.tk = tk
    self.root = root

    self.w = tk.Toplevel(width = 300, height = 500)
    self.lf = []
    self.x = []
    self.y = []
    self.vx = []
    self.vy = []

  def update(self, objects):

    if len(objects) != len(self.lf):
      for widget in self.lf:
        widget.destroy()
      self.lf = []
      for i, obj in enumerate(objects):
        lf = self.tk.LabelFrame(self.w, text=str(i+1), width = 300, height=200)
        lf.pack()
        self.lf.append(lf)

        var = self.tk.StringVar()
        label = self.tk.Label(lf, textvariable=var)
        label.pack()
        self.x.append(var)

        var = self.tk.StringVar()
        label = self.tk.Label(lf, textvariable=var)
        label.pack()
        self.y.append(var)

        var = self.tk.StringVar()
        label = self.tk.Label(lf, textvariable=var)
        label.pack()
        self.vx.append(var)

        var = self.tk.StringVar()
        label = self.tk.Label(lf, textvariable=var)
        label.pack()
        self.vy.append(var)

    for i, obj in enumerate(objects):
      self.x[i].set("x: " + str(obj.x))
      self.y[i].set("y: " + str(obj.y))
      self.vx[i].set("vx: " + str(obj.Vx))
      self.vy[i].set("vy: " + str(obj.Vy))
    return 0