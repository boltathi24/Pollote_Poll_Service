from flask import Flask
from myservice import database

from myservice.routes import create_poll
from myservice.routes import get_poll_with_category,get_poll_with_id,get_user,vote_poll




application=Flask(__name__)

@application.route("/api/polls/createPoll",methods=['POST'])
def createPoll():
    return create_poll.createPoll()

@application.route("/api/polls/votePoll",methods=['POST'])
def votePoll():
    return vote_poll.votePoll()

@application.route("/api/polls/getPollDetails/subcategory",methods=['GET'])
def getPollBySubCate():
    return get_poll_with_category.getPolls()

@application.route("/api/polls/getPollDetails/id",methods=['GET'])
def getPllById():
    return get_poll_with_id.getPolls()



@application.route("/api/polls/getMyPolls",methods=['POST'])
def getMyPoll():
    return get_user.getMyPolls()

@application.route("/api/polls/getVotedPolls",methods=['POST'])
def getVotedPolls():
    return get_user.myVotedPolls()





if __name__ == '__main__':
    application.run(debug=True)

