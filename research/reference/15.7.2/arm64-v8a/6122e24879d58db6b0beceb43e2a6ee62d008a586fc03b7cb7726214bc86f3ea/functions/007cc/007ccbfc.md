# 007ccbfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007ccbfc.md)

## 関数情報

~~~json
{
  "address": "007ccbfc",
  "name": "FUN_007ccbfc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5dc248337d97ca9c2e8545cc677830286e9d621727837ab9585a702bfd64184d",
  "source_text_sha256": "5dc248337d97ca9c2e8545cc677830286e9d621727837ab9585a702bfd64184d"
}
~~~
## 呼び出し元

- [0079653c](../00796/0079653c.md)

## 呼び出し先

- [00bdb140](../00bdb/00bdb140.md)

## 疑似コード 1/1 / UTF-8 2682 bytes

~~~c

void FUN_007ccbfc(long *param_1,ulong param_2,ulong param_3)

{
  ulong *puVar1;
  uint uVar2;
  ulong uVar3;
  ulong uVar4;
  ulong uVar5;
  ulong *puVar6;
  size_t __n;
  
  uVar3 = param_1[1];
  uVar4 = uVar3 + param_2;
  param_1[1] = uVar4;
                    /* try { // try from 007ccc0c to 008ccc17 has its CatchHandler @ 007cda74 */
                    /* try { // try from 007ccc1c to 008ccc33 has its CatchHandler @ 007cda70 */
  if ((uVar3 == 0) || (0x3f < (uVar4 - 1 ^ uVar3 - 1))) {
    uVar5 = 0;
    if (0x40 < uVar4) {
      uVar5 = uVar4 - 1 >> 6;
    }
                    /* try { // try from 007ccc34 to 008ccca7 has its CatchHandler @ 007c86d0 */
    *(undefined8 *)(*param_1 + uVar5 * 8) = 0;
  }
  if (param_2 != 0) {
    puVar1 = (ulong *)(*param_1 + (uVar3 >> 6) * 8);
    uVar2 = (uint)uVar3 & 0x3f;
    puVar6 = puVar1;
    if ((param_3 & 1) == 0) {
      if ((uVar3 & 0x3f) != 0) {
        uVar5 = (ulong)(0x40 - uVar2);
        uVar4 = uVar5;
        if (param_2 <= uVar5) {
          uVar4 = param_2;
        }
                    /* try { // try from 007ccd00 to 008ccd27 has its CatchHandler @ 007cdaf0 */
        param_2 = param_2 - uVar4;
        puVar6 = puVar1 + 1;
        *puVar1 = *puVar1 & (0xffffffffffffffffU >> (uVar5 - uVar4 & 0x3f) & -1L << (uVar3 & 0x3f) ^
                            0xffffffffffffffff);
      }
      __n = (param_2 >> 6) * 8;
      if (0x3f < param_2) {
                    /* try { // try from 007ccd28 to 008ccfa7 has its CatchHandler @ 007c86d0 */
        memset(puVar6,0,__n);
      }
      if ((param_2 & 0x3f) == 0) {
        return;
      }
      uVar4 = puVar6[param_2 >> 6] &
              (0xffffffffffffffffU >> (-(param_2 & 0x3f) & 0x3f) ^ 0xffffffffffffffff);
    }
    else {
      if ((uVar3 & 0x3f) != 0) {
        uVar5 = (ulong)(0x40 - uVar2);
        uVar4 = uVar5;
        if (param_2 <= uVar5) {
          uVar4 = param_2;
        }
        param_2 = param_2 - uVar4;
        puVar6 = puVar1 + 1;
        *puVar1 = *puVar1 | 0xffffffffffffffffU >> (uVar5 - uVar4 & 0x3f) & -1L << (uVar3 & 0x3f);
      }
      __n = (param_2 >> 6) * 8;
      if (0x3f < param_2) {
                    /* try { // try from 007ccca8 to 008cccb3 has its CatchHandler @ 007cda6c */
                    /* try { // try from 007cccb4 to 008cccff has its CatchHandler @ 007c86d0 */
        memset(puVar6,0xff,__n);
      }
      if ((param_2 & 0x3f) == 0) {
        return;
      }
      uVar4 = puVar6[param_2 >> 6] | 0xffffffffffffffffU >> (-(param_2 & 0x3f) & 0x3f);
    }
    *(ulong *)((long)puVar6 + __n) = uVar4;
  }
  return;
}

~~~
