use std::collections::BTreeMap;

// 件数と容量を制限し、最後に参照した順に保持する。
pub struct Cache<T> {
    entries: BTreeMap<String, (u64, usize, T)>,
    clock: u64,
    bytes: usize,
    limit: usize,
    capacity: usize,
    pub hits: u64,
    pub misses: u64,
}
impl<T> Cache<T> {
    pub fn new(capacity: usize, limit: usize) -> Self {
        Self {
            entries: BTreeMap::new(),
            clock: 0,
            bytes: 0,
            limit,
            capacity,
            hits: 0,
            misses: 0,
        }
    }
    pub fn get(&mut self, key: &str) -> Option<&T> {
        self.clock += 1;
        if let Some((used, _, value)) = self.entries.get_mut(key) {
            *used = self.clock;
            self.hits += 1;
            Some(value)
        } else {
            self.misses += 1;
            None
        }
    }
    pub fn insert(&mut self, key: String, value: T, bytes: usize) {
        if bytes > self.limit {
            return;
        }
        if let Some((_, size, _)) = self.entries.remove(&key) {
            self.bytes -= size;
        }
        self.clock += 1;
        self.bytes += bytes;
        self.entries.insert(key, (self.clock, bytes, value));
        while self.entries.len() > self.capacity || self.bytes > self.limit {
            let oldest = self
                .entries
                .iter()
                .min_by_key(|(_, (used, _, _))| used)
                .map(|(key, _)| key.clone())
                .unwrap();
            self.bytes -= self.entries.remove(&oldest).unwrap().1;
        }
    }
    pub fn clear(&mut self) {
        self.entries.clear();
        self.bytes = 0;
    }
    pub fn summary(&self) -> serde_json::Value {
        serde_json::json!({"entries":self.entries.len(),"bytes":self.bytes,"hits":self.hits,"misses":self.misses})
    }
}

#[test]
fn evicts_oldest_with_byte_limit() {
    let mut cache = Cache::new(2, 6);
    cache.insert("a".into(), 1, 2);
    cache.insert("b".into(), 2, 2);
    assert_eq!(cache.get("a"), Some(&1));
    cache.insert("c".into(), 3, 3);
    assert!(cache.get("b").is_none());
    assert_eq!(cache.get("a"), Some(&1));
    cache.insert("oversized".into(), 4, 7);
    assert!(cache.get("oversized").is_none());
}
