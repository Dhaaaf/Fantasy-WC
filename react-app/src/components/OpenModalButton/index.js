import React from 'react';
import { useModal } from '../../context/Modal';

function OpenModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose // optional: callback function that will be called once the modal is closed
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (onButtonClick) onButtonClick();
  };

  if (buttonText === "i") {
    // console.log("button text");
    return (
      <button
        onClick={onClick}
        className={`OpenModalButton-button ${buttonText}`}
      >
        <div className="i-container">
        <i className="fa-solid fa-info"></i>
        </div>
      </button>
    );
  }


  if (buttonText === "edit-league") {
    // console.log("button text");
    return (
      <button
        onClick={onClick}
        className={`OpenModalButton-button ${buttonText}`}
      >
        <div className="gear-container">
        <i className="fa-solid fa-gear"></i>
        </div>
      </button>
    );
  }

  if (buttonText === "edit-team-name") {
    // console.log("button text");
    return (
      <button
        onClick={onClick}
        className={`OpenModalButton-button ${buttonText}`}
      >
        <div className="name-edit-delete">
        <i className="fa-solid fa-pen-to-square"></i>
        </div>
      </button>
    );
  }

  if (buttonText === "leaderboard") {
    // console.log("button text");
    return (
      <button
        onClick={onClick}
        className={`OpenModalButton-button ${buttonText}`}
      >
        <div className="league-leaderboard-button">
          Leaderboard  <i className="fa-solid fa-table"></i>
        </div>
      </button>
    );
  }


  if (buttonText === "next-match-day") {
    // console.log("button text");
    return (
      <button
        onClick={onClick}
        className={`OpenModalButton-button ${buttonText}`}
      >
        <div className="next-matchday-button">
        Next Match Day  <i className="fa-solid fa-arrow-right"></i>
        </div>
      </button>
    );
  }

  return (
    <button onClick={onClick}>{buttonText}</button>
  );
}

export default OpenModalButton;
