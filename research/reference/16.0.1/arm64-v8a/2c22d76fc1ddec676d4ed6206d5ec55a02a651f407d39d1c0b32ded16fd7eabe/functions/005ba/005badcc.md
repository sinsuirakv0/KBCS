# 005badcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "005badcc",
  "name": "FUN_005badcc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3927f9875075bf785219f1a4e1220474854815864f78628d56406ed918b6ec2",
  "source_text_sha256": "e3927f9875075bf785219f1a4e1220474854815864f78628d56406ed918b6ec2"
}
~~~

## 呼び出し元

- [005ba958](../005ba/005ba958.md)

## 呼び出し先

- [00c58530](../00c58/00c58530.md)
- [00c58540](../00c58/00c58540.md)

## 疑似コード / UTF-8 260 bytes

~~~c

void FUN_005badcc(undefined8 param_1)

{
                    /* try { // try from 005badd4 to 006bade3 has its CatchHandler @ 005baec8 */
  _ZNSt6__ndk117__assoc_sub_state4waitEv();
  _ZNSt6__ndk117__assoc_sub_state16__on_zero_sharedEv(param_1);
  return;
}

~~~
