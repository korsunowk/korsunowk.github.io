import React from 'react'

import '../../../styles/modal-window.css'
import '../../../styles/buttons.css'

export default function ModalWindow (props) {
  let winBlock = (
    <div>
      <h1>Congratulations!</h1>
      <h2>You're passed the Speed Test!</h2>
      <div className='button-block'>
        <a className='button' href='/speed-test'>New</a>
        <a className='button' href='/table'>Go to table</a>
      </div>
    </div>
  )
  let loseBlock = (
    <div>
      <h1>Test is failed!</h1>
      <h2>Dont worry, you can retake the Speed Test!</h2>
      <div className='button-block'>
        <a className='button' href='/speed-test'>Retry</a>
        <a className='button' href='/table'>Go to table</a>
      </div>
    </div>
  )
  let displayedBlock = props.type === 'win' ? winBlock : loseBlock

  return (
    <div className={'modal-window ' + props.type}>
      {displayedBlock}
    </div>
  )
}
