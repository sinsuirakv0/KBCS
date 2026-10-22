# 004ceefc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](004ceefc.md)

## 関数情報

~~~json
{
  "address": "004ceefc",
  "name": "Botan::RSA_PublicKey::key_length",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc655c381ae9bc2c0fe2acee8e7b9b63e961ddf2c020e12aa16070b1789fb19d",
  "source_text_sha256": "dc655c381ae9bc2c0fe2acee8e7b9b63e961ddf2c020e12aa16070b1789fb19d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 1028 bytes

~~~c

/* virtual thunk to Botan::RSA_PublicKey::key_length() const */

long __thiscall Botan::RSA_PublicKey::key_length(RSA_PublicKey *this)

{
  uint uVar1;
  ulong uVar2;
  ulong uVar3;
  long lVar4;
  
  lVar4 = *(long *)(this + *(long *)(*(long *)this + -0x30) + 8);
  uVar2 = *(long *)(this + *(long *)(*(long *)this + -0x30) + 0x10) - lVar4 >> 2;
  uVar3 = uVar2;
  if (*(long *)(this + *(long *)(*(long *)this + -0x30) + 0x10) - lVar4 == 0) {
LAB_004cef38:
    if (uVar3 != 0) {
      uVar3 = uVar3 - 1;
      if (uVar3 < uVar2) {
        uVar1 = *(uint *)(lVar4 + uVar3 * 4);
      }
      else {
        uVar1 = 0;
      }
      lVar4 = 0x20;
      do {
        if ((uVar1 >> (ulong)((int)lVar4 - 1U & 0x1f) & 1) != 0) break;
        lVar4 = lVar4 + -1;
      } while (lVar4 != 0);
      return lVar4 + uVar3 * 0x20;
    }
  }
  else {
    do {
      if (*(int *)(lVar4 + -4 + uVar3 * 4) != 0) goto LAB_004cef38;
      uVar3 = uVar3 - 1;
    } while (uVar3 != 0);
  }
  return 0;
}

~~~
