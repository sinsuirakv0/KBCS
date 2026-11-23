# 006bffdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0120.md#review-6425f40a2e17ff4753e04f9a06b88666)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006bffdc",
  "name": "FUN_006bffdc",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3e19cccad81cb0b0aa8307e1f154eaebb0908321e17e2b3ea57460638eb10f5",
  "source_text_sha256": "d3e19cccad81cb0b0aa8307e1f154eaebb0908321e17e2b3ea57460638eb10f5"
}
~~~

## 呼び出し元

- [006bed1c](../006be/006bed1c.md)

## 呼び出し先

- [005e8158](../005e8/005e8158.md)

## 疑似コード / UTF-8 1846 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined8 FUN_006bffdc(int *param_1)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined1 auVar3 [16];
  undefined1 auVar4 [16];
  
                    /* try { // try from 006bffe0 to 007bffe3 has its CatchHandler @ 006c02cc */
  uVar1 = *(undefined8 *)param_1;
  auVar3._8_8_ = uVar1;
  auVar3._0_8_ = uVar1;
                    /* try { // try from 006bfff8 to 007bfffb has its CatchHandler @ 006c02ac */
  auVar4 = NEON_ushl(auVar3,_DAT_002c2d50,8);
                    /* try { // try from 006c0010 to 007c0017 has its CatchHandler @ 006c0274 */
  auVar3 = NEON_ushl(auVar3,_DAT_002c26e0,8);
                    /* try { // try from 006c002c to 007c002f has its CatchHandler @ 006c027c */
  uVar2 = NEON_ushl(CONCAT44(CONCAT13(auVar3[0xb] ^ auVar4[0xb],
                                      CONCAT12(auVar3[10] ^ auVar4[10],
                                               CONCAT11(auVar3[9] ^ auVar4[9],auVar3[8] ^ auVar4[8])
                                              )),
                             CONCAT13(auVar3[3] ^ auVar4[3],
                                      CONCAT12(auVar3[2] ^ auVar4[2],
                                               CONCAT11(auVar3[1] ^ auVar4[1],auVar3[0] ^ auVar4[0])
                                              ))),DAT_002c40c8,4);
                    /* try { // try from 006c0044 to 007c004b has its CatchHandler @ 006c025c */
  *param_1 = (((uint)(byte)((ulong)uVar1 >> 0x38) ^ (uint)uVar1) & 0xff |
              (uint)(uVar2 & 0xff00000000ff00) | (uint)((uVar2 & 0xff00000000ff00) >> 0x20) |
             ((uint)((ulong)uVar1 >> 0x20) ^ (uint)uVar1 >> 0x18) << 0x18) + 1;
  FUN_005e8158();
                    /* try { // try from 006c0060 to 007c0067 has its CatchHandler @ 006c0258 */
  return uVar1;
}

~~~
