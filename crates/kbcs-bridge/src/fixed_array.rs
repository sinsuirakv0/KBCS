use serde::{Deserialize, Deserializer, Serialize, Serializer, de::Error};

pub fn serialize<T: Serialize, S: Serializer, const N: usize>(
    value: &[T; N],
    serializer: S,
) -> Result<S::Ok, S::Error> {
    value.as_slice().serialize(serializer)
}

pub fn deserialize<'de, T: Deserialize<'de>, D: Deserializer<'de>, const N: usize>(
    deserializer: D,
) -> Result<[T; N], D::Error> {
    exact(Vec::deserialize(deserializer)?)
}

fn exact<T, E: Error, const N: usize>(values: Vec<T>) -> Result<[T; N], E> {
    values
        .try_into()
        .map_err(|values: Vec<T>| E::invalid_length(values.len(), &"fixed array"))
}

pub mod nested {
    use super::*;

    pub fn serialize<T: Serialize, S: Serializer, const N: usize>(
        value: &[[T; N]; 2],
        serializer: S,
    ) -> Result<S::Ok, S::Error> {
        [value[0].as_slice(), value[1].as_slice()].serialize(serializer)
    }

    pub fn deserialize<'de, T: Deserialize<'de>, D: Deserializer<'de>, const N: usize>(
        deserializer: D,
    ) -> Result<[[T; N]; 2], D::Error> {
        let [first, second] = <[Vec<T>; 2]>::deserialize(deserializer)?;
        Ok([exact(first)?, exact(second)?])
    }
}
