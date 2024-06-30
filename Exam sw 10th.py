from tkinter import *
import random
from tkinter import messagebox
import time
import threading
import sys
def countdown():
    global mytime
    mytime=1740
    for x in range(1740):
        mytime=mytime-1
        ltime.place(x=1000,y=10)
        ltime['text']=mytime
        time.sleep(1)
        if mytime==0 :
            messagebox.showinfo(title='Info',message="Time Over")
            break            
        if qn==25:
            break
  
def qLabel(j):
    l['text']=j
    l.place(x=50,y=100)    
    r.set(None)
def savescore():
    global score
    global t
    with open("/home/vaheeda/trendterm1/trend10a.txt","a") as f:
        data=t.get()+"  "+str(score)+"\n"
        f.write(data)
        f.close()
        messagebox.showinfo(title='Info',message="Your Score is "+str(score)+"/36")
        root.destroy()
        root.quit()
def bshortclick():
       
    global score
    global flag
    global l1
    global qn
    global qni
    global i
    global ans
    global t
    global ans1
    global k
   
    if mytime>0:
        shortbox1.place(x=600,y=400)
        shortbox2.place(x=700,y=400)
        bshortenter.place(x=650,y=500)
        bshort.place_forget()
        if qn<=24:
           l1['text']="Q No: " +str(qn)
           l1.place(x=800,y=10)
           for j,k in questions2[i].items():
               qLabel(j)
               passk(k)
           i=i+1
    
        if qn==25:
            l['text']="Finished "
            l.place(x=50,y=100)
            savescore()
            
            root.quit()
    
      
        
def bshortenterclick():
    global score
    global flag
    global flag1
    global l1
    global qn
    global qni
    global i
    global ans
    global t
    global ans1
    global a
    global b
    global ansr
    a=t1.get()+t2.get()
    b=a.lower()
    ans=b
    ansr=b[::-1]
    if qn>=17 and qn<=24:
        
        if k1=='A':
            ans1='ad'
        elif k1=='B':
            ans1='cd'
        elif k1=='C':
            ans1='cd'
        elif k1=='D':
            ans1='ab'
        elif k1=='E':
            ans1='ab'
        elif k1=='F':
            ans1='bd'
        elif k1=='G':
            ans1='ad'            
        elif k1=='H':
            ans1='bd'
        elif k1=='I':
            ans1='cd'
        elif k1=='J':
            ans1='ac'
        elif k1=='K':
            ans1='ae'
        elif k1=='L':
            ans1='ae'
        elif k1=='M':
            ans1='de'
        elif k1=='N':
            ans1='ae'
        elif k1=='O':
            ans1='ad'
        elif k1=='P':
            ans1='ae'
        elif k1=='Q':
            ans1='ae'
        elif k1=='R':
            ans1='ae'
        elif k1=='S':
            ans1='ae'
        elif k1=='T':
            ans1='ad'
        
        if t1.get()=="" or t2.get()=="":
            messagebox.showinfo(title='Info',message="Type your options in each of the boxes")
            flag1=1
        else:
            flag1=0
            if ans1==ans or ans1==ansr:
                flag=1
                score=score+1.5
                
            else:
                flag=0
        if flag==0 and flag1==0:    
            messagebox.showinfo(title='Info',message="Correct answer is  "+ans1)
            flag1=0
    shortbox1.delete(0,END)
    shortbox2.delete(0,END)
    if flag1==0:
        l['text']="   "    
        qn=qn+1
        bshortenter.place_forget()
        bshort.place(x=700,y=50)
        shortbox1.place_forget()
        shortbox2.place_forget()
def press1(event):
                        
    if len(shortbox1.get())>=1:
        messagebox.showinfo(title='Info',message="Enter only one option in each box")
        shortbox1.delete(0,END)
def press2(event):                        
    if len(shortbox2.get())>=1:
        messagebox.showinfo(title='Info',message="Enter only one option in each box")
        shortbox2.delete(0,END)
def bmultstartclick():
    global t
    global score
    global flag
    global l1
    global qn
    global qni
    global i
    global ans
    global chk
    global ch
    global k1
    global k2
    if qn==1:
        countdown_thread=threading.Thread(target=countdown)   
        countdown_thread.start()
    if mytime>0:
       if qn>1 and flag==0:
           messagebox.showinfo(title='Info',message="Correct answer is  "+k2)
           flag=2
       bmultstart['text']='Next'
       if chk!=ch:
           messagebox.showinfo(title='Info',message="Select Your Answer")
       else:
           if t.get():
              if qn<=16:
                 r1.pack()
                 r2.pack()
                 r3.pack()
                 r4.pack()
                 l1['text']="Q No: " +str(qn)
                 l1.place(x=800,y=10)
                 for j,k in questions[qni].items():
                    qLabel(j)
                    passk(k)
                    qni=qni+1
                    qn=qn+1
                    ch=qn
              elif qn==17:
                 l1['text']=" "
                 l1.place(x=800,y=10)
                 bmultstart.config(state='disabled')
                 bshort.place(x=700,y=50)
                 frame.destroy()
                 frame1.destroy()
                 frame2.destroy()
                 frame3.destroy()
                 j="Finished Multiple Choice Questions . Click 'Load Short Answer Questions'"
                 qLabel(j)
            
              if flag==1:
                 score=score+1.5
                 flag=0
              
       
           else:
              messagebox.showinfo(title='Info',message="Enter Your Name")
        
    
        
    
def radioclicked():
    global k1
    global flag
    global score
    global chk
    global ch
    global k2
    chk=ch
    if r.get()==k1:
        flag=1
        
    else:
        flag=0
    if k1=='1':
        k2='c'
    elif k1=='2':
        k2='d'
    elif k1=='3':
        k2='a'
    elif k1=='4':
        k2='b'    
def passk(k):
    global k1
    k1=k    
root=Tk()
root.title('test')
root.geometry('2000x1000')
root.configure(bg="#fff")
root.resizable(True,True)
global r
global score
global qn
global k1
global k
global ans1
global countdown_thread
flag=0
flag1=0
r=StringVar()
r.set(None)
t=StringVar()
t1=StringVar()
t2=StringVar()
k2=StringVar()
global ans
global st_time
i=0
qn=1
qni=0
score=0
chk=1
ch=1
global a
global b
global ansr
q1="""Which of the following is wrong statement.?

      a. svg pictures can be imported to different image sizes "
      b. Vector pictures can be prepared in Inkscape
      c. Clarity of svg pictures decreases when exported to bigger canvas.
      d. Images drawn in Inkscape can be exported to png format"""
q2="""Which of the following way can be used to align the letters into
      curve shape in Inkscape software?
      
        a) Text → Remove from path
        b) Text → Put on Path
        c) Text → Difference
        d) Text → Follow in to frame """
q3="""Which of the following combination of keys is used to along with the
      mouse to change the size of an object proportionally
     (in proportion to length and breadth) in Inkscape software?
     
        a) Shift + Space       b) Space + Ctrl
        c) Tab + Ctrl          d) Ctrl + Shift  """      
q4="""Which of the following is a WYSIWYG html editor with an open source licence?

     a. BlueGriffon         b. LibreOffice Impress
     c. Synfig Studio       d. Sunclock """
q5="""Which of the following way can be used to lighten the depth of a
      colour given to an object in Inkscape software?
      
        a) Increase the Opacity of the object.
        b) Decrease the Opacity of the object
        c) Zoom the Object
        d) Decrease the size of the stroke of the object."""
q6="""Which of the following tool is used to select objects in Inkscape software?

        a) Select and Transform Objects
        b) Edit paths by nodes
        c) Draw Bezier curves and straight lines
        d) Draw Calligraphic"""
q7="""A table of contents is prepared for a document about Democracy.
      Normally what style will be the Heading (Index) have?
      
      a. Contents Heading          b. Figure Index Heading
      c.  Heading 1                d. Header 1"""
q8="""Which one of the following is a Free Vector Image Editing software?

        a) Libre Office Draw       b) Corel Draw
        c) Gimp                    d) Adobe Illustrator."""
q9="""Which of the following tags can be used to include Cascading Styles
      in Internal method in a web stage?
      
      a. <css>…………</css>             b. <h3>…………</h3>         
      c. <style>………..</style>        d. <body>………..</body>"""
q10="""Which of the following can be used to colour the paragraph in a webpage
       with the colour#332211 using cascading style?
       
       a) p{color=#332211;}       b) p{color()#332211;}
       c) p{color;#332211;}       d) p{color:#332211;} """
q11="""Which of the following statements is true.

        a) Svg images are vector images.
        b) Vector images lose their clarity when zoomed in.
        c) Svg images are raster images.
        d) Bitmap images are also known as Vector image."""
q12="""Sonu is creating a picture in Inkscape. Which of the following can be done
       using the tools in the tab Stroke paint in Fill and Stroke window?

        a) Colour the object
        b) Remove the colour of the object
        c) Colour the outer line of the object
        d) Change the style of the object"""
q13="""What is the another name for raster images?

        a) Vector Images   b) Gif Images
        c) Bitmap Images   d) SVG Images   """      
q14="""A circle is drawn using Inkscape software. Which technique should be
        used to create an effect of a sphere by giving light and shade?

            a) Blur   b) Fill   c) Opacity   d) Gradient """
q15="""What is the name of the system that helps to build websites without
       learning scripting language?
       
      a) Web Content Management System
      b) Cascading Style Sheet
      c) Hyper Text Markup Language
      d) World Wide Web Consortium"""
q16="""Which of the of the following software has Mail Merge feature?

        a) LibreOffice writer    b) LibreOffice Impress
        c) Synfig Studio         d) Inkscape"""
q17="""Which of the following methods can be used to easily reach the
       corresponding page from the table of contents of a Word Processor document?

        a) Click on the heading with Ctrl key pressed.
        b) Click on the heading with shift key pressed.
        c) Click on the heading with F1 key pressed.
        d) Click on the heading with Enter key pressed."""
q18="""What does the Libre Office Writer software do when the Heading 1
       style in the  Style Box is applied to a text?
       
       a) Defines the selected text as the header of that page
       b) Defines the selected text as the header of every page
       c) Defines the selected text as the title
       d) Sets the selected text as the footer of that page"""
q19="""There is a project report prepared in Word Processor. Which of the following
        tool can be used for adding contents page in this file?

        a) Styles                        b) Paragraph Layout
        c) Table of Contents and Index   d) Clone Formatting"""
q20="""Which of the following methods can be used to make changes to the defined style,
        Heading1 in a Word Processor document?

        a) Select Clone Formatting and then click on the heading to be modified.
        b) Select the heading to be modified and click on Font Colour tool.
        c) Right click on Heading1 in Styles and click Modify.
        d) Click the tool, Export directly as PDF."""

q21="""Which of the following functions can be done using Mail Merge?

        a) To add data from a database to a text document
        b) To add from a text document to a database
        c) To search data for a report in a data base
        d) To change data from a database to another database """
q22="""While designing a Web page including cascading styles using Type Selector,
       a tag should be used within <style> to give a background color. Identify the tag.

        a) body {background : yellow;}       b) body [background: yellow;]
        c) body < background :yellow; >      d) body bgcolor=”yellow” """
q23="""Which of the following is the attribute used to define the background colour when
       a webpage is created with Cascading Style?

        a) background     b) backgroundcolour
        c) back-color     d) backcolor """
q24="""Radikha has defined a class selector for paragraph in her name for a webpage.
        Which of the following codes should be used to make the attributes displayed in the webpage?

        a) p.class=radikha      b) <p class = “radikha”>
        c) p< class=radikha>    d) <p radikha> """
q25="""Web Content Management Systems are mainly of three types. Online, Offline,…………………………….

            a) Inline   b) External    c) Selector    d) Hybrid"""
q26="""Which of the following can be used to give the font size 28px to h3 headings in a
       webpage using cascading styles?

            a) h3{font-size=28px;}       b) h3{size:28px;}
            c) h3{size=28px;}            d) h3{font-size:28px;}"""
q27="""Which of the following option should be used to properly align the various parts
        of an image created in Inkscape software and make them into a single unit?

            a) Mask   b) Group    c) Ungroup    d) Pattern"""
q28="""Which of the following keys can be used with mouse to colour the stroke of a picture
       in Inkscape using colour palette?

            a) Shift    b) Space   c) Tab   d) F1"""
q29="""Which of the following statement is correct regarding pixels in an image of size 100 x 30 pixels?

        a) The x axis will have 1000 pixels and the y axis will have 300 pixels
        b) The x axis will have 1000 pixels and the y axis will have 3000 pixels
        c) The x axis will have 100 pixels and the y axis will have 300 pixels
        d) The x axis will have 100 pixels and the y axis will have 30 pixels"""
q30="""In order to prepare health cards for students of a class, the fields in the file data.ods
        is added to the file healtcard.odt using the technique Mail Merge in Libre Office Writer.
        Which of the following is the next step to get the health cards?

        a) Click on Fields in Format Menu
        b) Click on Save in File menu
        c) Click on Export as PDF in File menu
        d) Click on Print in the File menu"""
q31="""Ami prepared a report with 25 pages of her school in Libre Office Writer. Which one is the tool to
       modify the headings in the same style and make the formatting faster?

        a) Styles and Formatting (Styles)     b) Paragraph Formatting
        c) Clone Formatting                   d) Page Formatting"""
q32="""While using Internal Cascading style, which of the following codes can be used for applying
        background colour in a webpage?

            a) <body style=”background: blue”>
            b) body{background:blue}
            c) body<<background:blue>>
            d) <style> body{background: blue;} </style>"""
q33="""When Manu was preparing a webpage, she used the name of the tag itself in the cascading styles for
        specifying the styles of the tag. In what name is this style known as?

            a) Internal CSS   b) Class Selector
            c) Type Selector  d) External CSS"""
q34="""Pick out the two correct statements regarding Raster Images from the following.

            a) Raster Images lose their clarity while scaling.
            b) Clarity of Raster images increases when it is zoomed in.
            c) Raster images maintain its clarity even when it is zoomed in.
            d) The images created in Gimp software are Raster images.
            e) svg Images are raster images. """ 
q35="""In order to make a tea cup using Inkscape software, two circles are drawn in the canvas.
       Now, we need to remove a portion of the bottom circle to a appropriate shape.
        Some activities on the worksheet prepared for this are incorrect. Which are they?

            a) Draw an oval and make a circle above it.
            b) Select both the circles using the selection tool.
            c) Click on union in path menu.
            d) Select only one circle using the selection tool.
            e) Click on difference in path menu. """
q36="""Choose the correct two statements related to Inkscape software from the following.

            a) Cannot Import Vector image
            b) Cannot Import bitmap image
            c) Facility to Import bitmap images and edit them
            d) Facility to convert vector images to Raster
            e) Vector images are created based on Pixels"""
q37="""Identify two most appropriate statements regarding the Index Table in a
        Word Processor document from the following.

        a) The Style of the title of the Index Table is usually included in the section Contents Heading.
        b) The headings in the Index Table should be in the Style Contents 1.
        c) The subheadings in the Index Table should be in the Style Header 1.
        d) The Style of the title of the Index Table is usually included in the section Index Heading.
        e) The sub headings in the Index Table should be in the style Index 1. """
q38="""The benefits of using Indexes and Tables in a document prepared in Libre Office Writer
        are given below. Choose the wrong ones.

        a) The table of contents will be in Malayalam irrespective of the document’s language.
        b) The table of contents can be made in any language irrespective of the document’s language.
        c) A specific page containing a heading can be reached by clicking on the heading holding the Ctrl
            key.
        d) We can easily understand the contents of the document and the starting page of each chapter.
        e) All the heading are arranged according to the page number without typing. """
q39="""The styles prepared by Sunil is given here.What changes will happen in the webpage. When these codes
           are used in it? Pick out from the following.
           
        <style>
           body{background:aqua;}
           h2{color:brown;background:gold;}
        </style>

        a) Webpage gets gold background colour.
        b) Headings gets gold background colour.
        c) Headings get gold colour.
        d) Web page gets aqua background colour.
        e) Headings get Aqua background colour
                     """
q40="""An html file contains the following codes.

            <p class=”first”>……….<p/>
            <p class=”second”>……….</p>     
Choose the true statements about the codes from the followings.

    a) These are Class selectors             b) These are type Selectors
    c) Same style is given to different headings of the same tag.
    d) Different style is given to different paragraphs of the same tag.
    e) These are included in the tag, <class>"""
q41="""Which of the following are the two methods used to give colour to the outline of
            an object in Inkscape Software?

        a) Select the object and click the colour palette.
        b) Select the object and use Fill and Stroke → Stroke Paint
        c) Select the object, hold the ctrl key and click on the colour palette.
        d) Select the object, hold the shift key and click on the colour palette.
        e) Select the object and use Fill and Stroke→Fill"""
q42="""Select two steps from the following to create text in arc shape according to the
        semi circle drawn,in Inkscape software.

        a) Select the text.
        b) Select object→ Group method.
        c) Select Text → Put on Path method.
        d) Select Text and semi circle.
        e) Select Path→ Difference Method"""
q43="""The certificates for children who have completed the Covid vaccination at school
        need to be prepared using the mail merge system in word processor. Which of the
        following files can be used for this?

        a) Students.ods file containing the details of students.
        b) Students.pdf file containing the details of students.
        c) Certificate.odt file containing a sample of the certificate.
        d) Certificate.pdf file containing a sample of the certificate
        e) Certificate.jpg file containing a sample of the certificate"""
q44="""The following are some of the techniques and its uses available in Libre office writer.
        Which of the following are correct?

        a) Clone Formatting- To apply the format of a given text or an object to another one.
        b) Mail Merge- To combine multiple cells in a table into a single cell
        c) Index table- To add data from a database to document.
        d) Formatting- To remove existing data in a database and new ones.
        e) Styles – Define headings, subheadings etc, and give them uniform format"""
q45="""Following are few of the steps to include external cascading styles in a webpage.
        Choose the right option from them.

        a) Prepare a file called styles.css including cascading styles.
        b) Include the tag <style> inside the tag <head> and define styles.
        c) Add <link rel=”stylesheet” type=”text/css” href=”style.css”>inside the tag<body>
        d) Add <link rel=”style.css” type=”text/css” href=”stylesheet”>inside the tag,<head>
        e) Add <link rel=”stylesheet” type=”text/css” href=”style.css”>inside the tag,<head>"""
q46="""Choose the right steps from the following to include internal cascading style in a web page.

        a) Create a cascading style sheet called style.css
        b) Define styles for the tags created.
        c) Include the tag.<style> inside the tag, <body>
        d) Include the tag, <style> inside the tag,<head>
        e) Include styles inside the tag, <style>"""
questions=[{q1:'1'},{q2:'4'},{q3:'2'},{q4:'3'},{q5:'4'},{q6:'3'},{q7:'3'},{q8:'3'},{q9:'1'},{q10:'2'},{q11:'3'},{q12:'1'},{q13:'1'},{q14:'2'},{q15:'3'},{q16:'3'},{q17:'3'},{q18:'1'},{q19:'1'},{q20:'1'},{q21:'3'},{q22:'3'},{q23:'3'},{q24:'4'},{q25:'2'},{q26:'2'},{q27:'4'},{q28:'3'},{q29:'2'},{q30:'2'},{q31:'3'},{q32:'2'},{q33:'1'}]
random.shuffle(questions)
questions2=[{q34:'A'},{q35:'B'},{q36:'C'},{q37:'D'},{q38:'E'},{q39:'F'},{q40:'G'},{q41:'H'},{q42:'I'},{q43:'J'},{q44:'K'},{q45:'L'},{q46:'M'}]
random.shuffle(questions2)
labelframe = LabelFrame(root, text=" ")
labelframe.pack(fill="both", expand="yes") 
l = Label(labelframe, text=" ",bg='cyan',height =14,width=80,fg='blue',font=('Microsoft Yahei UI Light',14))
frame=Frame(root)
frame.place(x=400,y=500)
frame1=Frame(root)
frame1.place(x=500,y=500)
frame2=Frame(root)
frame2.place(x=600,y=500)
frame3=Frame(root)
frame3.place(x=700,y=500)
frameentry=Frame(root)
frameentry.place(x=50,y=50)
l1=Label(root,text='0 ',bg='pink',fg="blue",font=('Microsoft Yahei UI Light',24))
ltime=Label(root,text='0 ',bg='pink',fg="blue",font=('Microsoft Yahei UI Light',24))
l2=Label(root,text='Enter Your Name',bg='pink',fg="Black",font=('Microsoft Yahei UI Light',15)).place(x=50,y=20)
namebox=Entry(frameentry,textvariable=t,width=15,font=('Microsoft Yahei UI Light',24)).pack(padx=5,pady=5)
shortbox1=Entry(root,textvariable=t1,width=3,highlightbackground="red",highlightcolor="red",font=('Microsoft Yahei UI Light',20))
shortbox2=Entry(root,textvariable=t2,width=3,highlightbackground="red",highlightcolor="red",font=('Microsoft Yahei UI Light',20))
shortbox1.bind('<Key>',press1)
shortbox2.bind('<Key>',press2)
bmultstart=Button(root,width=16,pady=5,text='Start Multiple Choice',bg='Green',fg='white',font=('Microsoft Yahei UI Light',14),border=0)
bmultstart.place(x=400,y=50)
bmultstart.config(command=bmultstartclick)
bshort=Button(root,width=16,pady=5,text='Load Short Answers',bg='Green',fg='white',font=('Microsoft Yahei UI Light',14),border=0)

bshort.config(command=bshortclick)
bshortenter=Button(root,width=20,pady=5,text='Submit',bg='Green',fg='white',font=('Microsoft Yahei UI Light',25),border=0)

bshortenter.config(command=bshortenterclick)

r1=Radiobutton(frame,text="a",variable=r,value=3,bg="Yellow",height=3,width=10,command=radioclicked)
r2=Radiobutton(frame1,text="b",variable=r,value=4,bg="Yellow",height=3,width=10,command=radioclicked)
r3=Radiobutton(frame2,text="c",variable=r,value=1,bg="Yellow",height=3,width=10,command=radioclicked)
r4=Radiobutton(frame3,text="d",variable=r,value=2,bg="Yellow",height=3,width=10,command=radioclicked)
root.mainloop()
         

