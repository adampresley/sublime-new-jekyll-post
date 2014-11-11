import sublime
import sublime_plugin

class NewJekyllPostCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("Starting NewJekyllPluginCommand...")
		buffer = self.window.new_file()
		buffer.run_command("new_jekyll_post_text")

class NewJekyllPostTextCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		template = """---
layout: post
title: Title
date: 2010-01-01 00:00
author: Adam Presley
tags: development
comments: true
---

New post!
"""

		self.view.insert(edit, 0, template)