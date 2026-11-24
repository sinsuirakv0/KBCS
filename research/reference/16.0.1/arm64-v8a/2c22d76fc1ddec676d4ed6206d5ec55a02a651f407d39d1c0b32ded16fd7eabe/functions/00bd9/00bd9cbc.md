# 00bd9cbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd9894`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd9/00bd9894.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0084.md#compare-696e0b423749341e629760127dbdf8f0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd9d58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9d58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-bc060bf1c038747f7422515e840ba9ba)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd9cbc",
  "name": "_ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc",
  "size": 332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c939a1459753a66de0b8f6118f169a6bedb647319a06aad4b1188fee662858cd",
  "source_text_sha256": "c939a1459753a66de0b8f6118f169a6bedb647319a06aad4b1188fee662858cd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd9cbc",
        "00bd9e07"
      ]
    ],
    "bytes_sha256": "efb7a189984a4fb2ee77b82777eaf3ea5dd7a9fea199881ec69355297392cdb8",
    "instruction_count": 83,
    "instruction_bytes": 332,
    "body_bytes": 332,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aba0](../00c5a/00c5aba0.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b260](../00c5b/00c5b260.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
"server_auth_code"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1633 bytes

~~~c

void _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc(undefined8 *param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  ulong uVar4;
  long lVar5;
  char *pcVar6;
  
  if (param_2 == 0) {
    pcVar6 = "server_auth_code";
  }
  else {
    if (DAT_01126cf8 != '\0') {
      lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar1 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
      uVar3 = (**(code **)(*plVar2 + 0x538))(plVar2,param_2);
      lVar1 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                        (plVar2,DAT_01126ae8,DAT_01126af8,uVar3);
      uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
      (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
      uVar3 = 0;
      if (((uVar4 & 1) == 0) && (lVar1 != 0)) {
        lVar5 = _ZN8firebase10app_common9GetAnyAppEv();
        if (lVar5 == 0) {
          _ZN8firebase9LogAssertEPKcz("app != nullptr");
        }
        plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar5);
        uVar3 = (**(code **)(*plVar2 + 0xa8))(plVar2,lVar1);
        (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
      }
      goto LAB_00bd9de4;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar6 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar6);
  uVar3 = 0;
LAB_00bd9de4:
  *param_1 = uVar3;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd9cbc"></a> `00bd9cbc` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bd9cc0"></a> `00bd9cc0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd9cc4"></a> `00bd9cc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd9cc8"></a> `00bd9cc8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bd9ccc"></a> `00bd9ccc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bd9cd0"></a> `00bd9cd0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bd9cd4"></a> `00bd9cd4` | `40 07 00 b4` | cbz x0,0x00bd9dbc | `CONDITIONAL_JUMP`
<a id="insn-00bd9cd8"></a> `00bd9cd8` | `68 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd9cdc"></a> `00bd9cdc` | `08 e1 73 39` | ldrb w8,[x8, #0xcf8] | `FALL_THROUGH`
<a id="insn-00bd9ce0"></a> `00bd9ce0` | `48 07 00 34` | cbz w8,0x00bd9dc8 | `CONDITIONAL_JUMP`
<a id="insn-00bd9ce4"></a> `00bd9ce4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd9ce8"></a> `00bd9ce8` | `5e 05 02 94` | bl 0x00c5b260 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9cec"></a> `00bd9cec` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd9cf0"></a> `00bd9cf0` | `80 00 00 b5` | cbnz x0,0x00bd9d00 | `CONDITIONAL_JUMP`
<a id="insn-00bd9cf4"></a> `00bd9cf4` | `c0 b6 ff b0` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bd9cf8"></a> `00bd9cf8` | `00 60 17 91` | add x0,x0,#0x5d8 | `FALL_THROUGH`
<a id="insn-00bd9cfc"></a> `00bd9cfc` | `c1 04 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9d00"></a> `00bd9d00` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd9d04"></a> `00bd9d04` | `df 04 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9d08"></a> `00bd9d08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd9d0c"></a> `00bd9d0c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd9d10"></a> `00bd9d10` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd9d14"></a> `00bd9d14` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bd9d18"></a> `00bd9d18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9d1c"></a> `00bd9d1c` | `68 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd9d20"></a> `00bd9d20` | `69 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd9d24"></a> `00bd9d24` | `01 75 45 f9` | ldr x1,[x8, #0xae8] | `FALL_THROUGH`
<a id="insn-00bd9d28"></a> `00bd9d28` | `22 7d 45 f9` | ldr x2,[x9, #0xaf8] | `FALL_THROUGH`
<a id="insn-00bd9d2c"></a> `00bd9d2c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd9d30"></a> `00bd9d30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd9d34"></a> `00bd9d34` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bd9d38"></a> `00bd9d38` | `9a 03 02 94` | bl 0x00c5aba0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9d3c"></a> `00bd9d3c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd9d40"></a> `00bd9d40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd9d44"></a> `00bd9d44` | `87 04 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9d48"></a> `00bd9d48` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd9d4c"></a> `00bd9d4c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bd9d50"></a> `00bd9d50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd9d54"></a> `00bd9d54` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bd9d58"></a> `00bd9d58` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd9d5c"></a> `00bd9d5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9d60"></a> `00bd9d60` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bd9d64"></a> `00bd9d64` | `17 04 00 37` | tbnz w23,#0x0,0x00bd9de4 | `CONDITIONAL_JUMP`
<a id="insn-00bd9d68"></a> `00bd9d68` | `f4 03 00 b4` | cbz x20,0x00bd9de4 | `CONDITIONAL_JUMP`
<a id="insn-00bd9d6c"></a> `00bd9d6c` | `3d 05 02 94` | bl 0x00c5b260 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9d70"></a> `00bd9d70` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd9d74"></a> `00bd9d74` | `80 00 00 b5` | cbnz x0,0x00bd9d84 | `CONDITIONAL_JUMP`
<a id="insn-00bd9d78"></a> `00bd9d78` | `c0 b6 ff b0` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bd9d7c"></a> `00bd9d7c` | `00 60 17 91` | add x0,x0,#0x5d8 | `FALL_THROUGH`
<a id="insn-00bd9d80"></a> `00bd9d80` | `a0 04 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9d84"></a> `00bd9d84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd9d88"></a> `00bd9d88` | `be 04 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9d8c"></a> `00bd9d8c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd9d90"></a> `00bd9d90` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd9d94"></a> `00bd9d94` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd9d98"></a> `00bd9d98` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bd9d9c"></a> `00bd9d9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9da0"></a> `00bd9da0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bd9da4"></a> `00bd9da4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd9da8"></a> `00bd9da8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bd9dac"></a> `00bd9dac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd9db0"></a> `00bd9db0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd9db4"></a> `00bd9db4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9db8"></a> `00bd9db8` | `0b 00 00 14` | b 0x00bd9de4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd9dbc"></a> `00bd9dbc` | `e0 b6 ff f0` | adrp x0,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bd9dc0"></a> `00bd9dc0` | `00 68 34 91` | add x0,x0,#0xd1a | `FALL_THROUGH`
<a id="insn-00bd9dc4"></a> `00bd9dc4` | `06 00 00 14` | b 0x00bd9ddc | `UNCONDITIONAL_JUMP`
<a id="insn-00bd9dc8"></a> `00bd9dc8` | `e0 b6 ff d0` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-00bd9dcc"></a> `00bd9dcc` | `00 40 38 91` | add x0,x0,#0xe10 | `FALL_THROUGH`
<a id="insn-00bd9dd0"></a> `00bd9dd0` | `b4 03 02 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9dd4"></a> `00bd9dd4` | `a0 b9 ff f0` | adrp x0,0x310000 | `FALL_THROUGH`
<a id="insn-00bd9dd8"></a> `00bd9dd8` | `00 c0 03 91` | add x0,x0,#0xf0 | `FALL_THROUGH`
<a id="insn-00bd9ddc"></a> `00bd9ddc` | `89 04 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9de0"></a> `00bd9de0` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bd9de4"></a> `00bd9de4` | `75 02 00 f9` | str x21,[x19] | `FALL_THROUGH`
<a id="insn-00bd9de8"></a> `00bd9de8` | `7f 0a 00 b9` | str wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd9dec"></a> `00bd9dec` | `7f fe 01 a9` | stp xzr,xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bd9df0"></a> `00bd9df0` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd9df4"></a> `00bd9df4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bd9df8"></a> `00bd9df8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd9dfc"></a> `00bd9dfc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd9e00"></a> `00bd9e00` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bd9e04"></a> `00bd9e04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd9cbc`](#insn-00bd9cbc) 範囲 `[['00bd9cbc', '00bd9cd7']]`
  - `CONDITIONAL_JUMP` [`00bd9cd4`](#insn-00bd9cd4) → [`00bd9dbc`](#insn-00bd9dbc)
  - `FALL_THROUGH` [`00bd9cd4`](#insn-00bd9cd4) → [`00bd9cd8`](#insn-00bd9cd8)
- ブロック [`00bd9cd8`](#insn-00bd9cd8) 範囲 `[['00bd9cd8', '00bd9ce3']]`
  - `CONDITIONAL_JUMP` [`00bd9ce0`](#insn-00bd9ce0) → [`00bd9dc8`](#insn-00bd9dc8)
  - `FALL_THROUGH` [`00bd9ce0`](#insn-00bd9ce0) → [`00bd9ce4`](#insn-00bd9ce4)
- ブロック [`00bd9ce4`](#insn-00bd9ce4) 範囲 `[['00bd9ce4', '00bd9cf3']]`
  - `CONDITIONAL_JUMP` [`00bd9cf0`](#insn-00bd9cf0) → [`00bd9d00`](#insn-00bd9d00)
  - `FALL_THROUGH` [`00bd9cf0`](#insn-00bd9cf0) → [`00bd9cf4`](#insn-00bd9cf4)
- ブロック [`00bd9cf4`](#insn-00bd9cf4) 範囲 `[['00bd9cf4', '00bd9cff']]`
  - `FALL_THROUGH` [`00bd9cfc`](#insn-00bd9cfc) → [`00bd9d00`](#insn-00bd9d00)
- ブロック [`00bd9d00`](#insn-00bd9d00) 範囲 `[['00bd9d00', '00bd9d67']]`
  - `CONDITIONAL_JUMP` [`00bd9d64`](#insn-00bd9d64) → [`00bd9de4`](#insn-00bd9de4)
  - `FALL_THROUGH` [`00bd9d64`](#insn-00bd9d64) → [`00bd9d68`](#insn-00bd9d68)
- ブロック [`00bd9d68`](#insn-00bd9d68) 範囲 `[['00bd9d68', '00bd9d6b']]`
  - `CONDITIONAL_JUMP` [`00bd9d68`](#insn-00bd9d68) → [`00bd9de4`](#insn-00bd9de4)
  - `FALL_THROUGH` [`00bd9d68`](#insn-00bd9d68) → [`00bd9d6c`](#insn-00bd9d6c)
- ブロック [`00bd9d6c`](#insn-00bd9d6c) 範囲 `[['00bd9d6c', '00bd9d77']]`
  - `CONDITIONAL_JUMP` [`00bd9d74`](#insn-00bd9d74) → [`00bd9d84`](#insn-00bd9d84)
  - `FALL_THROUGH` [`00bd9d74`](#insn-00bd9d74) → [`00bd9d78`](#insn-00bd9d78)
- ブロック [`00bd9d78`](#insn-00bd9d78) 範囲 `[['00bd9d78', '00bd9d83']]`
  - `FALL_THROUGH` [`00bd9d80`](#insn-00bd9d80) → [`00bd9d84`](#insn-00bd9d84)
- ブロック [`00bd9d84`](#insn-00bd9d84) 範囲 `[['00bd9d84', '00bd9dbb']]`
  - `UNCONDITIONAL_JUMP` [`00bd9db8`](#insn-00bd9db8) → [`00bd9de4`](#insn-00bd9de4)
- ブロック [`00bd9dbc`](#insn-00bd9dbc) 範囲 `[['00bd9dbc', '00bd9dc7']]`
  - `UNCONDITIONAL_JUMP` [`00bd9dc4`](#insn-00bd9dc4) → [`00bd9ddc`](#insn-00bd9ddc)
- ブロック [`00bd9dc8`](#insn-00bd9dc8) 範囲 `[['00bd9dc8', '00bd9ddb']]`
  - `FALL_THROUGH` [`00bd9dd8`](#insn-00bd9dd8) → [`00bd9ddc`](#insn-00bd9ddc)
- ブロック [`00bd9ddc`](#insn-00bd9ddc) 範囲 `[['00bd9ddc', '00bd9de3']]`
  - `FALL_THROUGH` [`00bd9de0`](#insn-00bd9de0) → [`00bd9de4`](#insn-00bd9de4)
- ブロック [`00bd9de4`](#insn-00bd9de4) 範囲 `[['00bd9de4', '00bd9e07']]`

## 命令位置別の参照

- [`00bd9cbc`](#insn-00bd9cbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9cc0`](#insn-00bd9cc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9cc4`](#insn-00bd9cc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9cc8`](#insn-00bd9cc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9cd4`](#insn-00bd9cd4) → [`00bd9dbc`](#insn-00bd9dbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9cdc`](#insn-00bd9cdc) → `01126cf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd9ce0`](#insn-00bd9ce0) → [`00bd9dc8`](#insn-00bd9dc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9ce8`](#insn-00bd9ce8) → [`00c5b260`](../00c5b/00c5b260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b260` · 推定シンボル `None` · 推定型 `None`
- [`00bd9cf0`](#insn-00bd9cf0) → [`00bd9d00`](#insn-00bd9d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9cf8`](#insn-00bd9cf8) → `002b25d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9cfc`](#insn-00bd9cfc) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d04`](#insn-00bd9d04) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d24`](#insn-00bd9d24) → `01126ae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd9d28`](#insn-00bd9d28) → `01126af8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd9d38`](#insn-00bd9d38) → [`00c5aba0`](../00c5a/00c5aba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aba0` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d44`](#insn-00bd9d44) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d64`](#insn-00bd9d64) → [`00bd9de4`](#insn-00bd9de4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d68`](#insn-00bd9d68) → [`00bd9de4`](#insn-00bd9de4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d6c`](#insn-00bd9d6c) → [`00c5b260`](../00c5b/00c5b260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b260` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d74`](#insn-00bd9d74) → [`00bd9d84`](#insn-00bd9d84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d7c`](#insn-00bd9d7c) → `002b25d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9d80`](#insn-00bd9d80) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bd9d88`](#insn-00bd9d88) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bd9db8`](#insn-00bd9db8) → [`00bd9de4`](#insn-00bd9de4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9dc0`](#insn-00bd9dc0) → `002b8d1a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9dc4`](#insn-00bd9dc4) → [`00bd9ddc`](#insn-00bd9ddc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9dcc`](#insn-00bd9dcc) → `002b7e10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9dd0`](#insn-00bd9dd0) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00bd9dd8`](#insn-00bd9dd8) → `003100f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9ddc`](#insn-00bd9ddc) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bd9df4`](#insn-00bd9df4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9df8`](#insn-00bd9df8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9dfc`](#insn-00bd9dfc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd9cbc`](#insn-00bd9cbc)

~~~json
{
  "source": "00bd9cbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9cc0`](#insn-00bd9cc0)

~~~json
{
  "source": "00bd9cc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9cc4`](#insn-00bd9cc4)

~~~json
{
  "source": "00bd9cc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9cc8`](#insn-00bd9cc8)

~~~json
{
  "source": "00bd9cc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9cd4`](#insn-00bd9cd4)

~~~json
{
  "source": "00bd9cd4",
  "target": "00bd9dbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9cdc`](#insn-00bd9cdc)

~~~json
{
  "source": "00bd9cdc",
  "target": "01126cf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126cf8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd9ce0`](#insn-00bd9ce0)

~~~json
{
  "source": "00bd9ce0",
  "target": "00bd9dc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9ce8`](#insn-00bd9ce8)

~~~json
{
  "source": "00bd9ce8",
  "target": "00c5b260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9cf0`](#insn-00bd9cf0)

~~~json
{
  "source": "00bd9cf0",
  "target": "00bd9d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9cf8`](#insn-00bd9cf8)

~~~json
{
  "source": "00bd9cf8",
  "target": "002b25d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b25d8",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b25d8",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd9cfc`](#insn-00bd9cfc)

~~~json
{
  "source": "00bd9cfc",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9d04`](#insn-00bd9d04)

~~~json
{
  "source": "00bd9d04",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9d24`](#insn-00bd9d24)

~~~json
{
  "source": "00bd9d24",
  "target": "01126ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd9d28`](#insn-00bd9d28)

~~~json
{
  "source": "00bd9d28",
  "target": "01126af8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126af8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd9d38`](#insn-00bd9d38)

~~~json
{
  "source": "00bd9d38",
  "target": "00c5aba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9d44`](#insn-00bd9d44)

~~~json
{
  "source": "00bd9d44",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9d64`](#insn-00bd9d64)

~~~json
{
  "source": "00bd9d64",
  "target": "00bd9de4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9d68`](#insn-00bd9d68)

~~~json
{
  "source": "00bd9d68",
  "target": "00bd9de4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9d6c`](#insn-00bd9d6c)

~~~json
{
  "source": "00bd9d6c",
  "target": "00c5b260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9d74`](#insn-00bd9d74)

~~~json
{
  "source": "00bd9d74",
  "target": "00bd9d84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9d7c`](#insn-00bd9d7c)

~~~json
{
  "source": "00bd9d7c",
  "target": "002b25d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b25d8",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b25d8",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd9d80`](#insn-00bd9d80)

~~~json
{
  "source": "00bd9d80",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9d88`](#insn-00bd9d88)

~~~json
{
  "source": "00bd9d88",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9db8`](#insn-00bd9db8)

~~~json
{
  "source": "00bd9db8",
  "target": "00bd9de4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9dc0`](#insn-00bd9dc0)

~~~json
{
  "source": "00bd9dc0",
  "target": "002b8d1a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8d1a",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "7365727665725f617574685f636f646500",
  "capture_start": "002b8d1a",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd9dc4`](#insn-00bd9dc4)

~~~json
{
  "source": "00bd9dc4",
  "target": "00bd9ddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9dcc`](#insn-00bd9dcc)

~~~json
{
  "source": "00bd9dcc",
  "target": "002b7e10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7e10",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "675f6d6574686f64735f63616368656400",
  "capture_start": "002b7e10",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd9dd0`](#insn-00bd9dd0)

~~~json
{
  "source": "00bd9dd0",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9dd8`](#insn-00bd9dd8)

~~~json
{
  "source": "00bd9dd8",
  "target": "003100f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003100f0",
  "offset": 0,
  "size": 97,
  "datatype": "string",
  "bytes": "4669726562617365204175746820776173206e6f7420696e697469616c697a65",
  "capture_start": "003100f0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd9ddc`](#insn-00bd9ddc)

~~~json
{
  "source": "00bd9ddc",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9df4`](#insn-00bd9df4)

~~~json
{
  "source": "00bd9df4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9df8`](#insn-00bd9df8)

~~~json
{
  "source": "00bd9df8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9dfc`](#insn-00bd9dfc)

~~~json
{
  "source": "00bd9dfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
