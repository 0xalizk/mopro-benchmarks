import matplotlib.pyplot as plt, math, numpy as np, sys, os
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
from matplotlib import rcParams
import matplotlib.font_manager as font_manager
from matplotlib.ticker import LogLocator
import toml, pprint, math

####################################################################################
def update_rcParams():
    rcParams['savefig.pad_inches'] = .2

    rcParams['axes.grid']          = True
    rcParams['axes.titlesize']     = 36
    rcParams['axes.labelsize']     = 28
    #font_path = os.getenv('HOME')+'/Library/Fonts/Ubuntu-Medium.ttf'
    #prop = font_manager.FontProperties(fname=font_path)
    #print(prop.get_name())
    try:
        rcParams['font.family'] = "Baloo Bhaina 2"#prop.get_name()
    except:
        pass

    # Adobe and Ubuntu are also good
    # rcParams['font.family']        = 'Adobe Caslon Pro'  # cursive, http://matplotlib.org/examples/pylab_examples/fonts_demo.html
    rcParams['font.serif']         = 'Helvetica' #['Bitstream Vera Sans', 'DejaVu Sans', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'sans-serif']

    rcParams['figure.titleweight']    = 'bold'
    rcParams['figure.titlesize']      = 45
    rcParams['figure.subplot.hspace'] = 0.9
    rcParams['figure.subplot.wspace'] = 0.1
    rcParams['figure.subplot.left']   = 0.1
    rcParams['figure.subplot.right']  = 0.9
    rcParams['figure.subplot.top']    = 0.90 # create a space between title and subplots
    rcParams['figure.subplot.bottom'] = 0.1

    rcParams['grid.alpha']         =  1
    rcParams['grid.color']         =  '#b3cccc' #'#63cae9'
    rcParams['grid.linestyle']     =  'solid' # dashed solid dashdot dotted
    rcParams['grid.linewidth']     =  0.5
    rcParams['axes.grid.axis']     =  'y'
    rcParams['axes.grid.which']    =  'both'


    rcParams['xtick.color']        =  'black'    #  ax.tick_params(axis='x', colors='red'). This will set both the tick and ticklabel to this color. To change labels' color, use: for t in ax.xaxis.get_ticklabels(): t.set_color('red')
    rcParams['xtick.direction']    =  'out'      # ax.get_yaxis().set_tick_params(which='both', direction='out')
    rcParams['xtick.labelsize']    =  22
    rcParams['xtick.major.pad']    =  1.0
    rcParams['xtick.major.size']   =  10.0      # how long the tick is
    rcParams['xtick.major.width']  =  1.0
    rcParams['xtick.minor.pad']    =  1.0
    rcParams['xtick.minor.size']   =  5.0
    rcParams['xtick.minor.width']  =  1
    rcParams['xtick.minor.visible']=  False


    rcParams['ytick.color']        =  'black'       # ax.tick_params(axis='x', colors='red')
    rcParams['ytick.direction']    =  'out'         # ax.get_xaxis().set_tick_params(which='both', direction='out')
    rcParams['ytick.labelsize']    =  22
    rcParams['ytick.major.pad']    =  4.0
    rcParams['ytick.major.size']   =  10.0
    rcParams['ytick.major.width']  =  1.0
    rcParams['ytick.minor.pad']    =  4.0
    rcParams['ytick.minor.size']   =  5
    rcParams['ytick.minor.width']  =  1
    rcParams['ytick.minor.visible']=  False


    rcParams['legend.borderaxespad']   =  0.5
    rcParams['legend.borderpad']       =  0.4
    rcParams['legend.columnspacing']   =  2.0
    rcParams['legend.edgecolor']       =  'inherit'
    rcParams['legend.facecolor']       =  'inherit'
    rcParams['legend.fancybox']        =  False
    rcParams['legend.fontsize']        =  30
    rcParams['legend.framealpha']      =  1
    rcParams['legend.frameon']         =  False
    rcParams['legend.handleheight']    =  0.7
    rcParams['legend.handlelength']    =  2.0
    rcParams['legend.handletextpad']   =  0.8
    #rcParams['legend.isaxes']          =  True
    rcParams['legend.labelspacing']    =  0.5
    rcParams['legend.markerscale']     =  1.0
    rcParams['legend.numpoints']       =  2
    rcParams['legend.scatterpoints']   =  3
    rcParams['legend.shadow']          =  False
####################################################################################
def plot(Ys, Xs, colors, ax):
    bar_width = 1
    for x,y,c in zip(Xs,Ys,colors):#i in range(len(Xs)):    
        ax.bar(x, y,  bar_width, color=c, linewidth=0, alpha=0.9) #,yerr=std_n2e, ecolor='black')   
####################################################################################
def beautify_ax(config, xticks):
    colors = config['style']['colors']
    labels = config['labels']['rows']
    groups = config['labels']['columns']
    ax.set_title(config['metadata']['title'], 
                 y=1.25,        # Vertical position (1.0 is default, higher values move it up)
                 pad=30,        # Padding between title and plot
                 fontsize=40)   # Font size of title

    
    ax.tick_params(labeltop=False)

    if 'log_scale' in config['metadata']:
        if config['metadata']['log_scale']:
            base = 10
            if 'log_base' in config['metadata']:
                base =  config['metadata']['log_base']
            ax.set_yscale('log', base=base)

    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())  
    ax.yaxis.get_major_formatter().set_scientific(False) 
    
    if "y_ticks" in config["style"]:
        ax.yaxis.set_major_locator(LogLocator(base=6))   
    ax.yaxis.set_minor_locator(ticker.NullLocator())  
    if 'y_ticks' in config['style']:
        ax.set_yticks(config['style']['y_ticks'])
    if 'y_tickslabels' in config['style']:
        ax.set_yticklabels(config['style']['y_tickslabels']) # must be after formatter setting
    
    ax.grid(True, axis='y', which='major')
    ax.grid(False, axis='y', which='minor')
    ax.set_xticks(xticks)
    #ax.set_xticklabels(BENCHS, rotation=45, ha='right')  # Rotate labels 45 degrees
    #print("\n"+str(groups)+"\n")
    ax.set_xticklabels(groups)
    ax.set_xlabel(config['metadata']['x_label'])
    ax.set_ylabel(config['metadata']['y_label']) 
    ax.tick_params(axis='x', 
                  which='both',
                  bottom=False,
                  top=False,           
                  labelbottom='on',
                  labeltop=False)      
    ax.tick_params(axis='y',
                  which='both',
                  left='on',
                  right='on',
                  labelleft='on',
                  labelright='on')
    patches =[]
    for c,l in zip(colors,labels):
        patches.append(mpatches.Patch(color =c, label=l))
    legend = plt.legend(
        handles=patches, 
        loc=(-.185, 1.05), 
        frameon=True,
        ncol=5,  # Make all patches appear in one line
        prop={'size': 25, 'family': rcParams['font.family']},  # Font size of legend text
        labelspacing=0.5,  # Vertical space between legend entries
        handlelength=1.8,  # Length of legend handles
        handletextpad=0.2,  # Space between handle and text
        #handletextpad=0.3 , # Space between handle and text, when patches are vertically stacked
        columnspacing=1.5,  # Space between columns
        borderpad=1.5,
    )
    frame = legend.get_frame()
    frame.set_linewidth(0)
    frame.set_facecolor('white')
    # Set y-axis limits to show all custom ticks
    # ax.set_ylim(8, 1200)  # Slightly below lowest and above highest tick
####################################################################################
def loadData(filename):
    if len(sys.argv) != 2:
        print("Usage: uv run main.py <../data/example.toml>")
        sys.exit(1)
    try:
        with open(filename, 'r') as f:
            config = toml.load(f)

        DATA = config['data']['dataset']
        if config['metadata'].get('transpose', False):  # Default to False if not specified
            config['data']['dataset'] = list(map(list, zip(*DATA)))
            
        """pp = pprint.PrettyPrinter(indent=2, width=80)
        print("\nParsed Configuration:")
        print("=" * 50)
        pp.pprint(config)
        print("=" * 50 + "\n")"""
        
        return config
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
####################################################################################
def save_ax():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
    plots_dir = os.path.join(parent_dir, "plots")
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)    
    file_name = sys.argv[1].split('/')[-1]
    save_path = plots_dir+'/' + '.'.join(file_name.split('.')[:-1]) + '.png'    
    print('plotted: ...' + save_path[int(0.5*len(save_path)):])
    plt.savefig(save_path, dpi=300, bbox_inches="tight") 
####################################################################################
if __name__ == '__main__':
    update_rcParams()

    config = loadData(sys.argv[1])
    
    fig = plt.figure(figsize=(60,60)) #inches
    ax = fig.add_axes([0.0015, 0.4862, 0.1700, 0.0915]) # (left, bottom, width, height) as a fraction of (figure figure width from left, figure height from bottom, figure width, figure height)

    xticks, pos       = [], 3 # 3 => pad between y-axis and first bar 
    for Ys in config['data']['dataset']:
        Xs = [i+pos for i in range(len(Ys))] # bar positions
        xticks.append (Xs[math.floor(len(Ys)/2)]) # one tick per group of bars
        plot(Ys, Xs, config['style']['colors'], ax)
        pos = 3 +  Xs[-1] # leave space between bar groups
    beautify_ax(config, xticks)
    save_ax()


