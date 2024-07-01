const taskListElement = document.querySelector('.list');
const taskElements = taskListElement.querySelectorAll('.item');

for (const task of taskElements) {
    task.draggable = true;
}

taskListElement.addEventListener('dragstart', (evt) => {
    evt.target.classList.add('selected');
});
  
taskListElement.addEventListener('dragend', (evt) => {
    evt.target.classList.remove('selected');
});

taskListElement.addEventListener('dragover', (evt) => {
    evt.preventDefault();

    const active = taskListElement.querySelector('.selected');
    const current = evt.target;
    const isMoveable = active !== current && current.classList.contains('item');

    if (!isMoveable) {
        return;
    }

    const next = (current === active.nextSibling) ?
        current.nextElementSibling :
        current;

    taskListElement.insertBefore(active, next);
});

const getNextElement = (cursorPosition, current) => {
    const currentCoord = current.getBoundingClientRect();
    const currentCenter = currentCoord.y + currentCoord.height / 2;
    const next = (cursorPosition < currentCenter) ? current : current.nextElementSibling;s
    return next;
};

tasksListElement.addEventListener('dragover', (evt) => {
    evt.preventDefault();
    const active = tasksListElement.querySelector('.selected');
    const current = evt.target;
    const isMoveable = active !== current &&
        current.classList.contains('item');

    if (!isMoveable) {
        return;
    }

    const next = getNextElement(evt.clientY, current);
    if ( next && (active === next.previousElementSibling || active === next)) {
        return;
    }
    tasksListElement.insertBefore(active, next);
});
