# 00b4cbfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b4cb34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cb34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0067.md#compare-620a5a60d48eb4248b3de8e83da3f4c8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4cc40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cc40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0068.md#compare-1d9ca49d86fff82a032b3d991eaae185)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cbfc",
  "name": "_ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb",
  "size": 320,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da3d741c05d436d71234534d6a1d96074f65230343a7e1c30553df8605f7b9de",
  "source_text_sha256": "da3d741c05d436d71234534d6a1d96074f65230343a7e1c30553df8605f7b9de",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4cbfc",
        "00b4cd3b"
      ]
    ],
    "bytes_sha256": "af5516c11e8052f4ec2d48cd03d9c45d37189a4ed3c1614a797715fdac485850",
    "instruction_count": 80,
    "instruction_bytes": 320,
    "body_bytes": 320,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddc40](../00bdd/00bddc40.md)

## 呼び出し先

- [00474b70](../00474/00474b70.md)
- [00551e14](../00551/00551e14.md)
- [00b4cda8](../00b4c/00b4cda8.md)
- [00bdddf0](../00bdd/00bdddf0.md)
- [00bde130](../00bde/00bde130.md)
- [00bde1b0](../00bde/00bde1b0.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1920 bytes

~~~c

void _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb(uint param_1)

{
  char cVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
                    /* try { // try from 00b4cc00 to 00c4cc6f has its CatchHandler @ 00b4ddd0 */
  if (DAT_010a1060 == 0) {
                    /* try { // try from 00b4cce8 to 00c4ccf3 has its CatchHandler @ 00b4da7c */
    DAT_010a1100 = 1;
    if ((param_1 & 1) == 0) {
      DAT_010a1100 = 2;
    }
  }
  else {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv(DAT_010a1060);
    if (DAT_010a1060 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
      if (DAT_010a1060 == 0) {
                    /* try { // try from 00b4cd34 to 00c4cd3f has its CatchHandler @ 00b4da38 */
        FUN_00551e14(uVar2,DAT_010a1098,DAT_010a0fd0,param_1 & 1);
        return;
      }
    }
    uVar3 = _ZNK8firebase3App9GetJNIEnvEv(DAT_010a1060);
    cVar1 = FUN_00474b70(uVar3,DAT_010a1098,DAT_010a0fc8);
    FUN_00551e14(uVar2,DAT_010a1098,DAT_010a0fd0,param_1 & 1);
    if (cVar1 != '\0') {
      return;
    }
                    /* try { // try from 00b4cc90 to 00c4cc9b has its CatchHandler @ 00b4db58 */
    if (DAT_010a1060 == 0) {
      _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
      _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
                    /* try { // try from 00b4ccb4 to 00c4ccbf has its CatchHandler @ 00b4dae8 */
      if (DAT_010a1060 == 0) goto LAB_00b4ccd4;
    }
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00b4ccc8 to 00c4cccb has its CatchHandler @ 00b4dac8 */
    cVar1 = FUN_00474b70(uVar2,DAT_010a1098,DAT_010a0fc8);
    if (cVar1 != '\0') {
LAB_00b4ccd4:
      FUN_00b4cda8();
      return;
    }
  }
                    /* try { // try from 00b4cd08 to 00c4cd13 has its CatchHandler @ 00b4da78 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4cbfc"></a> `00b4cbfc` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b4cc00"></a> `00b4cc00` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cc04"></a> `00b4cc04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4cc08"></a> `00b4cc08` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4cc0c"></a> `00b4cc0c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b4cc10"></a> `00b4cc10` | `b5 2a 00 b0` | adrp x21,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4cc14"></a> `00b4cc14` | `a8 32 40 f9` | ldr x8,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00b4cc18"></a> `00b4cc18` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00b4cc1c"></a> `00b4cc1c` | `68 06 00 b4` | cbz x8,0x00b4cce8 | `CONDITIONAL_JUMP`
<a id="insn-00b4cc20"></a> `00b4cc20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4cc24"></a> `00b4cc24` | `63 45 02 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cc28"></a> `00b4cc28` | `a8 32 40 f9` | ldr x8,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00b4cc2c"></a> `00b4cc2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b4cc30"></a> `00b4cc30` | `28 01 00 b5` | cbnz x8,0x00b4cc54 | `CONDITIONAL_JUMP`
<a id="insn-00b4cc34"></a> `00b4cc34` | `20 ba ff f0` | adrp x0,0x293000 | `FALL_THROUGH`
<a id="insn-00b4cc38"></a> `00b4cc38` | `00 b4 05 91` | add x0,x0,#0x16d | `FALL_THROUGH`
<a id="insn-00b4cc3c"></a> `00b4cc3c` | `6d 44 02 94` | bl 0x00bdddf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cc40"></a> `00b4cc40` | `a0 ba ff 90` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00b4cc44"></a> `00b4cc44` | `00 58 04 91` | add x0,x0,#0x116 | `FALL_THROUGH`
<a id="insn-00b4cc48"></a> `00b4cc48` | `3a 45 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cc4c"></a> `00b4cc4c` | `a8 32 40 f9` | ldr x8,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00b4cc50"></a> `00b4cc50` | `08 06 00 b4` | cbz x8,0x00b4cd10 | `CONDITIONAL_JUMP`
<a id="insn-00b4cc54"></a> `00b4cc54` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4cc58"></a> `00b4cc58` | `56 45 02 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cc5c"></a> `00b4cc5c` | `b7 2a 00 90` | adrp x23,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b4cc60"></a> `00b4cc60` | `b6 2a 00 b0` | adrp x22,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4cc64"></a> `00b4cc64` | `f7 22 3f 91` | add x23,x23,#0xfc8 | `FALL_THROUGH`
<a id="insn-00b4cc68"></a> `00b4cc68` | `c1 4e 40 f9` | ldr x1,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b4cc6c"></a> `00b4cc6c` | `e2 02 40 f9` | ldr x2,[x23] | `FALL_THROUGH`
<a id="insn-00b4cc70"></a> `00b4cc70` | `c0 9f e4 97` | bl 0x00474b70 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cc74"></a> `00b4cc74` | `c1 4e 40 f9` | ldr x1,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b4cc78"></a> `00b4cc78` | `e2 06 40 f9` | ldr x2,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00b4cc7c"></a> `00b4cc7c` | `17 1c 00 12` | and w23,w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4cc80"></a> `00b4cc80` | `63 02 00 12` | and w3,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00b4cc84"></a> `00b4cc84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4cc88"></a> `00b4cc88` | `63 14 e8 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cc8c"></a> `00b4cc8c` | `97 03 00 35` | cbnz w23,0x00b4ccfc | `CONDITIONAL_JUMP`
<a id="insn-00b4cc90"></a> `00b4cc90` | `a0 32 40 f9` | ldr x0,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00b4cc94"></a> `00b4cc94` | `20 01 00 b5` | cbnz x0,0x00b4ccb8 | `CONDITIONAL_JUMP`
<a id="insn-00b4cc98"></a> `00b4cc98` | `20 ba ff f0` | adrp x0,0x293000 | `FALL_THROUGH`
<a id="insn-00b4cc9c"></a> `00b4cc9c` | `00 b4 05 91` | add x0,x0,#0x16d | `FALL_THROUGH`
<a id="insn-00b4cca0"></a> `00b4cca0` | `54 44 02 94` | bl 0x00bdddf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cca4"></a> `00b4cca4` | `a0 ba ff 90` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00b4cca8"></a> `00b4cca8` | `00 58 04 91` | add x0,x0,#0x116 | `FALL_THROUGH`
<a id="insn-00b4ccac"></a> `00b4ccac` | `21 45 02 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ccb0"></a> `00b4ccb0` | `a0 32 40 f9` | ldr x0,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00b4ccb4"></a> `00b4ccb4` | `00 01 00 b4` | cbz x0,0x00b4ccd4 | `CONDITIONAL_JUMP`
<a id="insn-00b4ccb8"></a> `00b4ccb8` | `3e 45 02 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ccbc"></a> `00b4ccbc` | `a8 2a 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b4ccc0"></a> `00b4ccc0` | `c1 4e 40 f9` | ldr x1,[x22, #0x98] | `FALL_THROUGH`
<a id="insn-00b4ccc4"></a> `00b4ccc4` | `02 e5 47 f9` | ldr x2,[x8, #0xfc8] | `FALL_THROUGH`
<a id="insn-00b4ccc8"></a> `00b4ccc8` | `aa 9f e4 97` | bl 0x00474b70 | `UNCONDITIONAL_CALL`
<a id="insn-00b4cccc"></a> `00b4cccc` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4ccd0"></a> `00b4ccd0` | `60 01 00 54` | b.eq 0x00b4ccfc | `CONDITIONAL_JUMP`
<a id="insn-00b4ccd4"></a> `00b4ccd4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4ccd8"></a> `00b4ccd8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4ccdc"></a> `00b4ccdc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cce0"></a> `00b4cce0` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b4cce4"></a> `00b4cce4` | `31 00 00 14` | b 0x00b4cda8 | `CALL_TERMINATOR`
<a id="insn-00b4cce8"></a> `00b4cce8` | `7f 02 00 72` | tst w19,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ccec"></a> `00b4ccec` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ccf0"></a> `00b4ccf0` | `08 15 88 1a` | cinc w8,w8,eq | `FALL_THROUGH`
<a id="insn-00b4ccf4"></a> `00b4ccf4` | `a9 2a 00 b0` | adrp x9,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4ccf8"></a> `00b4ccf8` | `28 01 01 b9` | str w8,[x9, #0x100] | `FALL_THROUGH`
<a id="insn-00b4ccfc"></a> `00b4ccfc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4cd00"></a> `00b4cd00` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4cd04"></a> `00b4cd04` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cd08"></a> `00b4cd08` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b4cd0c"></a> `00b4cd0c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b4cd10"></a> `00b4cd10` | `a8 2a 00 b0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4cd14"></a> `00b4cd14` | `a9 2a 00 90` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b4cd18"></a> `00b4cd18` | `01 4d 40 f9` | ldr x1,[x8, #0x98] | `FALL_THROUGH`
<a id="insn-00b4cd1c"></a> `00b4cd1c` | `22 e9 47 f9` | ldr x2,[x9, #0xfd0] | `FALL_THROUGH`
<a id="insn-00b4cd20"></a> `00b4cd20` | `63 02 00 12` | and w3,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00b4cd24"></a> `00b4cd24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4cd28"></a> `00b4cd28` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b4cd2c"></a> `00b4cd2c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4cd30"></a> `00b4cd30` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cd34"></a> `00b4cd34` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b4cd38"></a> `00b4cd38` | `37 14 e8 17` | b 0x00551e14 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4cbfc`](#insn-00b4cbfc) 範囲 `[['00b4cbfc', '00b4cbff']]`
  - `FALL_THROUGH` [`00b4cbfc`](#insn-00b4cbfc) → [`00b4cc00`](#insn-00b4cc00)
- ブロック [`00b4cc00`](#insn-00b4cc00) 範囲 `[['00b4cc00', '00b4cc1f']]`
  - `CONDITIONAL_JUMP` [`00b4cc1c`](#insn-00b4cc1c) → [`00b4cce8`](#insn-00b4cce8)
  - `FALL_THROUGH` [`00b4cc1c`](#insn-00b4cc1c) → [`00b4cc20`](#insn-00b4cc20)
- ブロック [`00b4cc20`](#insn-00b4cc20) 範囲 `[['00b4cc20', '00b4cc33']]`
  - `CONDITIONAL_JUMP` [`00b4cc30`](#insn-00b4cc30) → [`00b4cc54`](#insn-00b4cc54)
  - `FALL_THROUGH` [`00b4cc30`](#insn-00b4cc30) → [`00b4cc34`](#insn-00b4cc34)
- ブロック [`00b4cc34`](#insn-00b4cc34) 範囲 `[['00b4cc34', '00b4cc53']]`
  - `CONDITIONAL_JUMP` [`00b4cc50`](#insn-00b4cc50) → [`00b4cd10`](#insn-00b4cd10)
  - `FALL_THROUGH` [`00b4cc50`](#insn-00b4cc50) → [`00b4cc54`](#insn-00b4cc54)
- ブロック [`00b4cc54`](#insn-00b4cc54) 範囲 `[['00b4cc54', '00b4cc8f']]`
  - `CONDITIONAL_JUMP` [`00b4cc8c`](#insn-00b4cc8c) → [`00b4ccfc`](#insn-00b4ccfc)
  - `FALL_THROUGH` [`00b4cc8c`](#insn-00b4cc8c) → [`00b4cc90`](#insn-00b4cc90)
- ブロック [`00b4cc90`](#insn-00b4cc90) 範囲 `[['00b4cc90', '00b4cc97']]`
  - `CONDITIONAL_JUMP` [`00b4cc94`](#insn-00b4cc94) → [`00b4ccb8`](#insn-00b4ccb8)
  - `FALL_THROUGH` [`00b4cc94`](#insn-00b4cc94) → [`00b4cc98`](#insn-00b4cc98)
- ブロック [`00b4cc98`](#insn-00b4cc98) 範囲 `[['00b4cc98', '00b4ccb3']]`
  - `FALL_THROUGH` [`00b4ccb0`](#insn-00b4ccb0) → [`00b4ccb4`](#insn-00b4ccb4)
- ブロック [`00b4ccb4`](#insn-00b4ccb4) 範囲 `[['00b4ccb4', '00b4ccb7']]`
  - `CONDITIONAL_JUMP` [`00b4ccb4`](#insn-00b4ccb4) → [`00b4ccd4`](#insn-00b4ccd4)
  - `FALL_THROUGH` [`00b4ccb4`](#insn-00b4ccb4) → [`00b4ccb8`](#insn-00b4ccb8)
- ブロック [`00b4ccb8`](#insn-00b4ccb8) 範囲 `[['00b4ccb8', '00b4ccc7']]`
  - `FALL_THROUGH` [`00b4ccc4`](#insn-00b4ccc4) → [`00b4ccc8`](#insn-00b4ccc8)
- ブロック [`00b4ccc8`](#insn-00b4ccc8) 範囲 `[['00b4ccc8', '00b4ccd3']]`
  - `CONDITIONAL_JUMP` [`00b4ccd0`](#insn-00b4ccd0) → [`00b4ccfc`](#insn-00b4ccfc)
  - `FALL_THROUGH` [`00b4ccd0`](#insn-00b4ccd0) → [`00b4ccd4`](#insn-00b4ccd4)
- ブロック [`00b4ccd4`](#insn-00b4ccd4) 範囲 `[['00b4ccd4', '00b4cce7']]`
- ブロック [`00b4cce8`](#insn-00b4cce8) 範囲 `[['00b4cce8', '00b4ccfb']]`
  - `FALL_THROUGH` [`00b4ccf8`](#insn-00b4ccf8) → [`00b4ccfc`](#insn-00b4ccfc)
- ブロック [`00b4ccfc`](#insn-00b4ccfc) 範囲 `[['00b4ccfc', '00b4cd07']]`
  - `FALL_THROUGH` [`00b4cd04`](#insn-00b4cd04) → [`00b4cd08`](#insn-00b4cd08)
- ブロック [`00b4cd08`](#insn-00b4cd08) 範囲 `[['00b4cd08', '00b4cd0f']]`
- ブロック [`00b4cd10`](#insn-00b4cd10) 範囲 `[['00b4cd10', '00b4cd33']]`
  - `FALL_THROUGH` [`00b4cd30`](#insn-00b4cd30) → [`00b4cd34`](#insn-00b4cd34)
- ブロック [`00b4cd34`](#insn-00b4cd34) 範囲 `[['00b4cd34', '00b4cd3b']]`

## 命令位置別の参照

- [`00b4cbfc`](#insn-00b4cbfc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc00`](#insn-00b4cc00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc04`](#insn-00b4cc04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc08`](#insn-00b4cc08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc14`](#insn-00b4cc14) → `010a1060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc1c`](#insn-00b4cc1c) → [`00b4cce8`](#insn-00b4cce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc24`](#insn-00b4cc24) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc28`](#insn-00b4cc28) → `010a1060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc30`](#insn-00b4cc30) → [`00b4cc54`](#insn-00b4cc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc38`](#insn-00b4cc38) → `0029316d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4cc3c`](#insn-00b4cc3c) → [`00bdddf0`](../00bdd/00bdddf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddf0` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc44`](#insn-00b4cc44) → `002a0116`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4cc48`](#insn-00b4cc48) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc4c`](#insn-00b4cc4c) → `010a1060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc50`](#insn-00b4cc50) → [`00b4cd10`](#insn-00b4cd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc58`](#insn-00b4cc58) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc68`](#insn-00b4cc68) → `010a1098`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc6c`](#insn-00b4cc6c) → `010a0fc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc70`](#insn-00b4cc70) → [`00474b70`](../00474/00474b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00474b70` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc74`](#insn-00b4cc74) → `010a1098`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc78`](#insn-00b4cc78) → `010a0fd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc88`](#insn-00b4cc88) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc8c`](#insn-00b4cc8c) → [`00b4ccfc`](#insn-00b4ccfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc90`](#insn-00b4cc90) → `010a1060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cc94`](#insn-00b4cc94) → [`00b4ccb8`](#insn-00b4ccb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cc9c`](#insn-00b4cc9c) → `0029316d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4cca0`](#insn-00b4cca0) → [`00bdddf0`](../00bdd/00bdddf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddf0` · 推定シンボル `None` · 推定型 `None`
- [`00b4cca8`](#insn-00b4cca8) → `002a0116`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ccac`](#insn-00b4ccac) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccb0`](#insn-00b4ccb0) → `010a1060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ccb4`](#insn-00b4ccb4) → [`00b4ccd4`](#insn-00b4ccd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccb8`](#insn-00b4ccb8) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccc0`](#insn-00b4ccc0) → `010a1098`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ccc4`](#insn-00b4ccc4) → `010a0fc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ccc8`](#insn-00b4ccc8) → [`00474b70`](../00474/00474b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00474b70` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccd0`](#insn-00b4ccd0) → [`00b4ccfc`](#insn-00b4ccfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccd4`](#insn-00b4ccd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccd8`](#insn-00b4ccd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccdc`](#insn-00b4ccdc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cce4`](#insn-00b4cce4) → [`00b4cda8`](00b4cda8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b4cda8` · 推定シンボル `None` · 推定型 `None`
- [`00b4ccf8`](#insn-00b4ccf8) → `010a1100`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00b4ccfc`](#insn-00b4ccfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd00`](#insn-00b4cd00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd04`](#insn-00b4cd04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd18`](#insn-00b4cd18) → `010a1098`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cd1c`](#insn-00b4cd1c) → `010a0fd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4cd28`](#insn-00b4cd28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd2c`](#insn-00b4cd2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd30`](#insn-00b4cd30) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cd38`](#insn-00b4cd38) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4cbfc`](#insn-00b4cbfc)

~~~json
{
  "source": "00b4cbfc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc00`](#insn-00b4cc00)

~~~json
{
  "source": "00b4cc00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc04`](#insn-00b4cc04)

~~~json
{
  "source": "00b4cc04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc08`](#insn-00b4cc08)

~~~json
{
  "source": "00b4cc08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc14`](#insn-00b4cc14)

~~~json
{
  "source": "00b4cc14",
  "target": "010a1060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc1c`](#insn-00b4cc1c)

~~~json
{
  "source": "00b4cc1c",
  "target": "00b4cce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc24`](#insn-00b4cc24)

~~~json
{
  "source": "00b4cc24",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cc28`](#insn-00b4cc28)

~~~json
{
  "source": "00b4cc28",
  "target": "010a1060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc30`](#insn-00b4cc30)

~~~json
{
  "source": "00b4cc30",
  "target": "00b4cc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc38`](#insn-00b4cc38)

~~~json
{
  "source": "00b4cc38",
  "target": "0029316d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029316d",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "0029316d",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4cc3c`](#insn-00b4cc3c)

~~~json
{
  "source": "00b4cc3c",
  "target": "00bdddf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cc44`](#insn-00b4cc44)

~~~json
{
  "source": "00b4cc44",
  "target": "002a0116",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0116",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002a0116",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4cc48`](#insn-00b4cc48)

~~~json
{
  "source": "00b4cc48",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cc4c`](#insn-00b4cc4c)

~~~json
{
  "source": "00b4cc4c",
  "target": "010a1060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc50`](#insn-00b4cc50)

~~~json
{
  "source": "00b4cc50",
  "target": "00b4cd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc58`](#insn-00b4cc58)

~~~json
{
  "source": "00b4cc58",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cc68`](#insn-00b4cc68)

~~~json
{
  "source": "00b4cc68",
  "target": "010a1098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1098",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc6c`](#insn-00b4cc6c)

~~~json
{
  "source": "00b4cc6c",
  "target": "010a0fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0fc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc70`](#insn-00b4cc70)

~~~json
{
  "source": "00b4cc70",
  "target": "00474b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cc74`](#insn-00b4cc74)

~~~json
{
  "source": "00b4cc74",
  "target": "010a1098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1098",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc78`](#insn-00b4cc78)

~~~json
{
  "source": "00b4cc78",
  "target": "010a0fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0fd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc88`](#insn-00b4cc88)

~~~json
{
  "source": "00b4cc88",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cc8c`](#insn-00b4cc8c)

~~~json
{
  "source": "00b4cc8c",
  "target": "00b4ccfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc90`](#insn-00b4cc90)

~~~json
{
  "source": "00b4cc90",
  "target": "010a1060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cc94`](#insn-00b4cc94)

~~~json
{
  "source": "00b4cc94",
  "target": "00b4ccb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cc9c`](#insn-00b4cc9c)

~~~json
{
  "source": "00b4cc9c",
  "target": "0029316d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029316d",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "0029316d",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4cca0`](#insn-00b4cca0)

~~~json
{
  "source": "00b4cca0",
  "target": "00bdddf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4cca8`](#insn-00b4cca8)

~~~json
{
  "source": "00b4cca8",
  "target": "002a0116",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0116",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002a0116",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4ccac`](#insn-00b4ccac)

~~~json
{
  "source": "00b4ccac",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ccb0`](#insn-00b4ccb0)

~~~json
{
  "source": "00b4ccb0",
  "target": "010a1060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ccb4`](#insn-00b4ccb4)

~~~json
{
  "source": "00b4ccb4",
  "target": "00b4ccd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ccb8`](#insn-00b4ccb8)

~~~json
{
  "source": "00b4ccb8",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ccc0`](#insn-00b4ccc0)

~~~json
{
  "source": "00b4ccc0",
  "target": "010a1098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1098",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ccc4`](#insn-00b4ccc4)

~~~json
{
  "source": "00b4ccc4",
  "target": "010a0fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0fc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ccc8`](#insn-00b4ccc8)

~~~json
{
  "source": "00b4ccc8",
  "target": "00474b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ccd0`](#insn-00b4ccd0)

~~~json
{
  "source": "00b4ccd0",
  "target": "00b4ccfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ccd4`](#insn-00b4ccd4)

~~~json
{
  "source": "00b4ccd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ccd8`](#insn-00b4ccd8)

~~~json
{
  "source": "00b4ccd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ccdc`](#insn-00b4ccdc)

~~~json
{
  "source": "00b4ccdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cce4`](#insn-00b4cce4)

~~~json
{
  "source": "00b4cce4",
  "target": "00b4cda8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ccf8`](#insn-00b4ccf8)

~~~json
{
  "source": "00b4ccf8",
  "target": "010a1100",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1100",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ccfc`](#insn-00b4ccfc)

~~~json
{
  "source": "00b4ccfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd00`](#insn-00b4cd00)

~~~json
{
  "source": "00b4cd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd04`](#insn-00b4cd04)

~~~json
{
  "source": "00b4cd04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd18`](#insn-00b4cd18)

~~~json
{
  "source": "00b4cd18",
  "target": "010a1098",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1098",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cd1c`](#insn-00b4cd1c)

~~~json
{
  "source": "00b4cd1c",
  "target": "010a0fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0fd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4cd28`](#insn-00b4cd28)

~~~json
{
  "source": "00b4cd28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd2c`](#insn-00b4cd2c)

~~~json
{
  "source": "00b4cd2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd30`](#insn-00b4cd30)

~~~json
{
  "source": "00b4cd30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cd38`](#insn-00b4cd38)

~~~json
{
  "source": "00b4cd38",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
