function ActionDeterminator() {
    var cbUpdate = document.getElementById("updatedb").checked;

    if(cbUpdate == false) {
        document.getElementById('logForm').action = '/autolog/add';
    }
    if(cbUpdate == true) {
        document.getElementById('logForm').action = '/autolog/update';
    }
}
