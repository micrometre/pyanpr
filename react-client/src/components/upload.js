import React, { useState } from "react";

export default function Uploader() {
    return (
        <>
            <form>
                <h1>React File Upload</h1>
                <input type="file" />
                <button type="submit">Upload</button>
            </form>
        </>
    );
}
