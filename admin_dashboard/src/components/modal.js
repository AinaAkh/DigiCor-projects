import {React , useState} from 'react';
import { Button, Modal }from 'react-bootstrap';
import "bootstrap/dist/css/bootstrap.min.css";

function ModalComponent( props ) {

    const [show, setShow] = useState(false)
    const buttonName = props.name
    const data = props.data
    const bomsData = [];

    return (
      <>
        <Button onClick={() => setShow(true)}>{buttonName}</Button>
        <Modal
          size="lg"
          show={show}
          onHide={() => setShow(false)}
          aria-labelledby="example-modal-sizes-title-lg"
        >
          <Modal.Header closeButton>
            <Modal.Title id="example-modal-sizes-title-lg">
              Null boms id's
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
          </Modal.Body>
        </Modal>
      </>
    );
  }

export default ModalComponent;