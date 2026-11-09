# 00afd6dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afd6dc",
  "name": "FUN_00afd6dc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b283d2841ac50dc91d8787489f7a6c9af75d6c2d3745393a8541305a76c16cd",
  "source_text_sha256": "6b283d2841ac50dc91d8787489f7a6c9af75d6c2d3745393a8541305a76c16cd"
}
~~~

## 呼び出し元

- [00710298](../00710/00710298.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afd6dc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b40);
}

~~~
