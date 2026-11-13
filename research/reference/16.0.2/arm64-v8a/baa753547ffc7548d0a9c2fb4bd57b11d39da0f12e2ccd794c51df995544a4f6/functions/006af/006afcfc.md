# 006afcfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006afcfc",
  "name": "FUN_006afcfc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c862b96561b042ff24601d730f0ff6c0829bde97d8091241f6f187bc360918f",
  "source_text_sha256": "1c862b96561b042ff24601d730f0ff6c0829bde97d8091241f6f187bc360918f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_006afcfc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c75e50;
  puVar1[1] = uVar2;
  return;
}

~~~
