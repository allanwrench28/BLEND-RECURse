// AI API Dropdown Menu Implementation

import React, { useState } from 'react';

const AiApiDropdown = ({ onApiSelect }) => {
    const [customApi, setCustomApi] = useState('');

    const predefinedApis = [
        'codestral/GHST',
        'mistralai/Devstral-Small-2505',
        'openai/gpt-4',
        'huggingface/starcoder'
    ];

    const handleApiChange = (event) => {
        const selectedApi = event.target.value;
        if (selectedApi === 'custom') {
            setCustomApi('');
        } else {
            onApiSelect(selectedApi);
        }
    };

    const handleCustomApiChange = (event) => {
        setCustomApi(event.target.value);
    };

    const handleCustomApiSubmit = () => {
        if (customApi.trim()) {
            onApiSelect(customApi);
        }
    };

    return (
        <div>
            <label htmlFor="api-dropdown">Select AI API:</label>
            <select id="api-dropdown" onChange={handleApiChange}>
                {predefinedApis.map((api) => (
                    <option key={api} value={api}>{api}</option>
                ))}
                <option value="custom">Custom API</option>
            </select>

            {customApi !== null && (
                <div>
                    <input
                        type="text"
                        placeholder="Enter custom API"
                        value={customApi}
                        onChange={handleCustomApiChange}
                    />
                    <button onClick={handleCustomApiSubmit}>Submit</button>
                </div>
            )}
        </div>
    );
};

export default AiApiDropdown;
