document.addEventListener("DOMContentLoaded", loadNotes);

function loadNotes() {
    fetch("/api/notes")
        .then(response => response.json())
        .then(notes => {
            const notesList = document.getElementById("notesList");
            notesList.innerHTML = "";
            notes.forEach(note => {
                const li = document.createElement("li");
                li.innerHTML = `
                    <span>${note.content}</span>
                    <div>
                        <button class="edit-button small" onclick="showEditNote(${note.id}, '${note.content}')">Edit</button>
                        <button class="delete-button small" onclick="deleteNote(${note.id})">Delete</button>
                    </div>
                `;
                notesList.appendChild(li);
            });
        });
}

function addNote() {
    const content = document.getElementById("noteContent").value;
    if (!content) return;

    fetch("/api/add_note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content })
    }).then(() => {
        document.getElementById("noteContent").value = "";
        loadNotes();
    });
}

function showEditNote(id, oldContent) {
    document.getElementById("editNoteId").value = id;
    document.getElementById("editNoteContent").value = oldContent;
    
    document.getElementById("updateNoteSection").style.display = "block";
}

function updateNote() {
    const id = document.getElementById("editNoteId").value;
    const newContent = document.getElementById("editNoteContent").value;

    fetch("/api/update_note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, content: newContent })
    }).then(() => {
        cancelEdit();
        loadNotes();
    });
}

function cancelEdit() {
    document.getElementById("updateNoteSection").style.display = "none";
}

function deleteNote(id) {
    if (!confirm("Are you sure you want to delete this note?")) return;

    fetch("/api/delete_note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id })
    }).then(() => loadNotes());
}
