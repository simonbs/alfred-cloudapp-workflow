alfred-cloudapp-workflow
========================

A workflow for Alfred 2.0 for uploading files to CloudApp. And more.

![](http://f.cl.ly/items/2U1V3K1O1a0k401Y0u3Z/alfred-cloudapp-workflow.png)

Features
===

Two file actions to upload a file to CloudApp. One action uploads as a public file while to other uploads the file as privately.
View items recently uploaded to CloudApp and select one to copy the URL to the item.
Send a bookmark to CloudApp. This is practically a very cool URL shortener. Especially if you have your own domain attached to your CloudApp account.
You do make mistakes, right? And you don’t want those mistakes on the interwebs, right? Delete items which were recently uploaded. 

Commands
===
- **cloud** Lists the recently uploaded files. Selecting one will copy the URL to the clipboard.
- **bookmark (url)** Bookmarks the URL and copies the URL to the clipboard. This can be disabled in config.json.
- **delcloud** Lists the recently uploaded files. Selecting one will delete the file from CloudApp.
- And of course, files can be uploaded to CloudApp from the file actions.
Installation

The workflow is written in Python and uses pycloudapp by Luis Nell. Because I have modified this wrapper a bit to get private file uploads working, this is bundled in the workflow. You do however need to install `poster` which the wrapper uses. This is easily done using the *easy_install* command. If you don’t have *easy_install* installed (you probably do if you ever write Python scripts :-)), you can grab it here and follow the installation instructions.

Fire up a terminal and write:
	
	easy_install poster

You’ll probably need to use sudo.

Now you’re ready to configure the workflow.

Either download the workflow or grab the source code.

If you downloaded the workflow with a *.alfredworkflow* extension, you must change the extension to *.zip* and decompress the archive. This probably created a directory. If so, open it.

Now, copy the file config.temp.json and rename it to *config.json*. Fill in your username and password for CloudApp. Your username is probably your e-mail address.
The attribute ‘copy_to_clipboard’ defines whether or not the URL should be copied to your clipboard when a file has been uploaded or a bookmark has been created. You can disable this, if you don’t want that behaviour.

Now you’re almost done. Select all the files in the directory, right click them and choose “Create archive”. Change the extension of the newly created archive from .zip to .alfredworkflow. It is important that you do not archive the folder but only its contents.

Double click the file you just created and you’re done :-)

About
===
This workflow is developed by [@simonbs](http://twitter.com/simonbs).