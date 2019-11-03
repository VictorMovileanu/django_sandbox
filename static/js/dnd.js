let dragSrcEl = null;
function handleDragStart(e) {
    dragSrcEl = this;
    e.dataTransfer.effectAllowed = 'move';
}
function handleDragEnd(e) {
    dragSrcEl = null;
}
function allowDrop(e) {
    e.preventDefault();
}
function handleDrop(e) {
    if (e.stopPropagation) {
        e.stopPropagation()
    }
    const url = this.dataset.updateurl;
    $.post(url);
    dragSrcEl = null;
}
[].forEach.call($('.link'), function (item) {
    item.addEventListener('dragstart', handleDragStart, false);
    item.addEventListener('dragend', handleDragEnd, false);
});
[].forEach.call($('.category'), function (item) {
    item.addEventListener('dragover', allowDrop, false);
    item.addEventListener('drop', handleDrop, false);
});