# 00bdebf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdebf0.md)

## 関数情報

~~~json
{
  "address": "00bdebf0",
  "name": "firebase::CleanupNotifier::UnregisterAllOwners",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "458a38a4a175dd322a58cd52904845fc74810fa46604d9d7a9df1e2f94d06ea9",
  "source_text_sha256": "458a38a4a175dd322a58cd52904845fc74810fa46604d9d7a9df1e2f94d06ea9"
}
~~~
## 呼び出し元

- [00afc4e4](../00afc/00afc4e4.md)

## 呼び出し先

- [00afc63c](../00afc/00afc63c.md)

## 疑似コード 1/1 / UTF-8 160 bytes

~~~c

void __thiscall firebase::CleanupNotifier::UnregisterAllOwners(CleanupNotifier *this)

{
  (*(code *)PTR_UnregisterAllOwners_00c1de30)();
  return;
}

~~~
