public static Boolean isValid(UserDO user) {
    if (Objects.isNull(user)) {
        return false;
    }
    return Boolean.TRUE.equals(user.getIsValid());
}

// Calls code.
UserDO user = ...;
Boolean isValid = isValid(user);
if (Objects.nonNull(isValid) && isValid.booleanValue()) { 
    ...
}
public static boolean isValid(UserDO user) {
    if (Objects.isNull(user)) {
        return false;
    }
    return Boolean.TRUE.equals(user.getIsValid());
}

// Calls code.
UserDO user = ...;
if (isValid(user)) {
    ...
}
