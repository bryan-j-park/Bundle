from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.goal_models import Goal
from flask_app.models.user_models import User