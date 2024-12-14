% rebase('_base.tpl')

<div>
    <h1>File Upload Vulnerabilty</h1>
    <form enctype="multipart/form-data" action="/file-upload/file_upload" method="POST">
        Upload an Image
        <br><br>
        <input name="input" type="file" accept=".jpg, .jpeg, .png"><br>
        <br>
        <input type="submit" name="upload" value="Upload">
    </form>
    % if output:
    <p>
        {{ output }}
    </p>
    % end
</div>