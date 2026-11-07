function getUserNames(users) {
    const names = [];

    for (let i = 0; i <= users.length; i++) {
        names.push(users[i].name);
    }

    return names;
}

const users = [
    { name: "Aytac" },
    { name: "Leyla" },
    { name: "Nigar" }
];

const result = getUserNames(users);

console.log("User names:", result);
