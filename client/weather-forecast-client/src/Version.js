import React from 'react';

function Version() {
    return (
        <div>
            <h1>Version Information</h1>
            <p>App Version: {process.env.REACT_APP_VERSION}</p>
        </div>
    );
}

export default Version;