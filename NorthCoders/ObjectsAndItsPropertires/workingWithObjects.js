function createPirate() {
    const pirateProfile = {
        realName: 'Edward Teach',
        shipName: 'La Concorde',
        treasure: {
            gems: 10,
            piecesOf8: 7,
            goldCoins: 150
        }
    };
    pirateProfile.pirateName = 'Blackbeard'
    delete pirateProfile.realName
    pirateProfile.treasure.piecesOf8 = 8
    pirateProfile.shipName = "Queen Anne's Revenge"
    return pirateProfile;
}
console.log(createPirate())