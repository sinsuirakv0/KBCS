# 007ffabc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "007ffabc",
  "name": "FUN_007ffabc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a13e584f36685892168231473bb38016c1d10a91b3ae9492429bde0f0371b1d5",
  "source_text_sha256": "a13e584f36685892168231473bb38016c1d10a91b3ae9492429bde0f0371b1d5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb60](../0043b/0043bb60.md)
- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 928 bytes

~~~c

undefined8 * FUN_007ffabc(long param_1)

{
  byte bVar1;
  undefined1 uVar2;
  undefined8 *puVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
                    /* try { // try from 007ffac0 to 008ffb23 has its CatchHandler @ 007ff698 */
  puVar3 = (undefined8 *)_Znwm(0x30);
  bVar1 = *(byte *)(param_1 + 0x18);
  uVar4 = *(undefined8 *)(param_1 + 8);
  uVar2 = *(undefined1 *)(param_1 + 0x10);
  *puVar3 = &PTR_FUN_00c7e400;
  puVar3[1] = uVar4;
  *(undefined1 *)(puVar3 + 2) = uVar2;
  if ((bVar1 & 1) == 0) {
    uVar5 = *(undefined8 *)(param_1 + 0x18);
    uVar4 = *(undefined8 *)(param_1 + 0x28);
    puVar3[4] = *(undefined8 *)(param_1 + 0x20);
    puVar3[3] = uVar5;
    puVar3[5] = uVar4;
  }
  else {
    FUN_0043bb60(puVar3 + 3,*(undefined8 *)(param_1 + 0x28),*(undefined8 *)(param_1 + 0x20));
  }
                    /* try { // try from 007ffb24 to 008ffb7b has its CatchHandler @ 007ffdf8 */
  return puVar3;
}

~~~
