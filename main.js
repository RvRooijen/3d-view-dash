const socket = io.connect('http://localhost:5000');

function initializeViewer() {
    const options = {
        env: 'AutodeskProduction',
        getAccessToken: function(onTokenReady) {
            const token = 'YOUR_ACCESS_TOKEN';
            const timeInSeconds = 3600;
            onTokenReady(token, timeInSeconds);
        }
    };

    Autodesk.Viewing.Initializer(options, function() {
        const viewerDiv = document.getElementById('3d-viewer');
        const viewer = new Autodesk.Viewing.GuiViewer3D(viewerDiv);
        viewer.start();

        const documentId = 'urn:YOUR_URN_ID';
        Autodesk.Viewing.Document.load(documentId, function(doc) {
            const viewables = doc.getRoot().getDefaultGeometry();
            viewer.loadDocumentNode(doc, viewables);
        });

        viewer.addEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, function(event) {
            const dbIdArray = event.dbIdArray;
            if (dbIdArray.length > 0) {
                const dbId = dbIdArray[0];
                socket.emit('js_event', { dbId: dbId });
            }
        });
    });
}

socket.on('dash_event', function(data) {
    console.log('Received event from Dash:', data);
    // Handle actions from Dash application here
});

initializeViewer();
