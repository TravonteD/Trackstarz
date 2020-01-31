import React from 'react';
import StatusUpdate from './StatusUpdate.js'
import FeedCard from './FeedCard.js'

function Feed() {
  return (
    <div className='col-lg-6 col-sm-12'>
    <div className='feed'>
    <StatusUpdate/>
    <FeedCard/>
    </div>
    </div>
  )
}

export default Feed;
