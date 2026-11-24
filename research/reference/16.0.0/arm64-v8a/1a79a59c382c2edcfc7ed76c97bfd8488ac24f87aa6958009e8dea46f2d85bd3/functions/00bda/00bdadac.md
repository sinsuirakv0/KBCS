# 00bdadac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6b8ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b8ac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-ef1528aeb6d6b48122fc5d71bcdb9527)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdb1d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb1d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-e758c4212576f5f5edd02076714f551e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdadac",
  "name": "_ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fbbdfca050cb9da1b4c93d144e5db05abcb2fefb35f1d9793fd4e1613913cfd",
  "source_text_sha256": "5fbbdfca050cb9da1b4c93d144e5db05abcb2fefb35f1d9793fd4e1613913cfd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdadac",
        "00bdae93"
      ]
    ],
    "bytes_sha256": "b05e0d705e29152292e82aaeea33deb12a8fce55ae47daa7b4d5930481df510e",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5ae60](../00c5a/00c5ae60.md)
- [00c5d730](../00c5d/00c5d730.md)
- [00c5da00](../00c5d/00c5da00.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1121 bytes

~~~c

void _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_
               (undefined8 param_1,undefined8 param_2,long *param_3,long param_4)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined1 auStack_88 [40];
  byte local_60;
  void *local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  if (param_4 == 0) {
    uVar4 = 0;
  }
  else {
    lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar2 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
    uVar4 = (**(code **)(*plVar3 + 0xa8))(plVar3,param_4);
    (**(code **)(*plVar3 + 0xb8))(plVar3,param_4);
  }
  _ZN8firebase4auth19PhoneAuthCredentialC2EPv(auStack_88,uVar4);
  (**(code **)(*param_3 + 0x10))(param_3,auStack_88);
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  _ZN8firebase4auth10CredentialD2Ev(auStack_88);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdadac"></a> `00bdadac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bdadb0"></a> `00bdadb0` | `f7 2b 00 f9` | str x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdadb4"></a> `00bdadb4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdadb8"></a> `00bdadb8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdadbc"></a> `00bdadbc` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdadc0"></a> `00bdadc0` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bdadc4"></a> `00bdadc4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdadc8"></a> `00bdadc8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bdadcc"></a> `00bdadcc` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bdadd0"></a> `00bdadd0` | `a8 83 1c f8` | stur x8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bdadd4"></a> `00bdadd4` | `c3 02 00 b4` | cbz x3,0x00bdae2c | `CONDITIONAL_JUMP`
<a id="insn-00bdadd8"></a> `00bdadd8` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bdaddc"></a> `00bdaddc` | `21 00 02 94` | bl 0x00c5ae60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdade0"></a> `00bdade0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdade4"></a> `00bdade4` | `80 00 00 b5` | cbnz x0,0x00bdadf4 | `CONDITIONAL_JUMP`
<a id="insn-00bdade8"></a> `00bdade8` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdadec"></a> `00bdadec` | `00 60 16 91` | add x0,x0,#0x598 | `FALL_THROUGH`
<a id="insn-00bdadf0"></a> `00bdadf0` | `84 ff 01 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdadf4"></a> `00bdadf4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdadf8"></a> `00bdadf8` | `a2 ff 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdadfc"></a> `00bdadfc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdae00"></a> `00bdae00` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdae04"></a> `00bdae04` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdae08"></a> `00bdae08` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdae0c"></a> `00bdae0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdae10"></a> `00bdae10` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdae14"></a> `00bdae14` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdae18"></a> `00bdae18` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdae1c"></a> `00bdae1c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdae20"></a> `00bdae20` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdae24"></a> `00bdae24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdae28"></a> `00bdae28` | `02 00 00 14` | b 0x00bdae30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdae2c"></a> `00bdae2c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bdae30"></a> `00bdae30` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdae34"></a> `00bdae34` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdae38"></a> `00bdae38` | `3e 0a 02 94` | bl 0x00c5d730 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae3c"></a> `00bdae3c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdae40"></a> `00bdae40` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bdae44"></a> `00bdae44` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdae48"></a> `00bdae48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdae4c"></a> `00bdae4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdae50"></a> `00bdae50` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdae54"></a> `00bdae54` | `68 00 00 36` | tbz w8,#0x0,0x00bdae60 | `CONDITIONAL_JUMP`
<a id="insn-00bdae58"></a> `00bdae58` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdae5c"></a> `00bdae5c` | `15 f3 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae60"></a> `00bdae60` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdae64"></a> `00bdae64` | `e7 0a 02 94` | bl 0x00c5da00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae68"></a> `00bdae68` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bdae6c"></a> `00bdae6c` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bdae70"></a> `00bdae70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdae74"></a> `00bdae74` | `e1 00 00 54` | b.ne 0x00bdae90 | `CONDITIONAL_JUMP`
<a id="insn-00bdae78"></a> `00bdae78` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdae7c"></a> `00bdae7c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdae80"></a> `00bdae80` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdae84"></a> `00bdae84` | `f7 2b 40 f9` | ldr x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdae88"></a> `00bdae88` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bdae8c"></a> `00bdae8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdae90"></a> `00bdae90` | `14 f3 01 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdadac`](#insn-00bdadac) 範囲 `[['00bdadac', '00bdadd7']]`
  - `CONDITIONAL_JUMP` [`00bdadd4`](#insn-00bdadd4) → [`00bdae2c`](#insn-00bdae2c)
  - `FALL_THROUGH` [`00bdadd4`](#insn-00bdadd4) → [`00bdadd8`](#insn-00bdadd8)
- ブロック [`00bdadd8`](#insn-00bdadd8) 範囲 `[['00bdadd8', '00bdade7']]`
  - `CONDITIONAL_JUMP` [`00bdade4`](#insn-00bdade4) → [`00bdadf4`](#insn-00bdadf4)
  - `FALL_THROUGH` [`00bdade4`](#insn-00bdade4) → [`00bdade8`](#insn-00bdade8)
- ブロック [`00bdade8`](#insn-00bdade8) 範囲 `[['00bdade8', '00bdadf3']]`
  - `FALL_THROUGH` [`00bdadf0`](#insn-00bdadf0) → [`00bdadf4`](#insn-00bdadf4)
- ブロック [`00bdadf4`](#insn-00bdadf4) 範囲 `[['00bdadf4', '00bdae2b']]`
  - `UNCONDITIONAL_JUMP` [`00bdae28`](#insn-00bdae28) → [`00bdae30`](#insn-00bdae30)
- ブロック [`00bdae2c`](#insn-00bdae2c) 範囲 `[['00bdae2c', '00bdae2f']]`
  - `FALL_THROUGH` [`00bdae2c`](#insn-00bdae2c) → [`00bdae30`](#insn-00bdae30)
- ブロック [`00bdae30`](#insn-00bdae30) 範囲 `[['00bdae30', '00bdae57']]`
  - `CONDITIONAL_JUMP` [`00bdae54`](#insn-00bdae54) → [`00bdae60`](#insn-00bdae60)
  - `FALL_THROUGH` [`00bdae54`](#insn-00bdae54) → [`00bdae58`](#insn-00bdae58)
- ブロック [`00bdae58`](#insn-00bdae58) 範囲 `[['00bdae58', '00bdae5f']]`
  - `FALL_THROUGH` [`00bdae5c`](#insn-00bdae5c) → [`00bdae60`](#insn-00bdae60)
- ブロック [`00bdae60`](#insn-00bdae60) 範囲 `[['00bdae60', '00bdae77']]`
  - `CONDITIONAL_JUMP` [`00bdae74`](#insn-00bdae74) → [`00bdae90`](#insn-00bdae90)
  - `FALL_THROUGH` [`00bdae74`](#insn-00bdae74) → [`00bdae78`](#insn-00bdae78)
- ブロック [`00bdae78`](#insn-00bdae78) 範囲 `[['00bdae78', '00bdae8f']]`
- ブロック [`00bdae90`](#insn-00bdae90) 範囲 `[['00bdae90', '00bdae93']]`

## 命令位置別の参照

- [`00bdadb0`](#insn-00bdadb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadb4`](#insn-00bdadb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadb8`](#insn-00bdadb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadbc`](#insn-00bdadbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadd0`](#insn-00bdadd0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadd4`](#insn-00bdadd4) → [`00bdae2c`](#insn-00bdae2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaddc`](#insn-00bdaddc) → [`00c5ae60`](../00c5a/00c5ae60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae60` · 推定シンボル `None` · 推定型 `None`
- [`00bdade4`](#insn-00bdade4) → [`00bdadf4`](#insn-00bdadf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadec`](#insn-00bdadec) → `002b2598`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdadf0`](#insn-00bdadf0) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bdadf8`](#insn-00bdadf8) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdae28`](#insn-00bdae28) → [`00bdae30`](#insn-00bdae30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae38`](#insn-00bdae38) → [`00c5d730`](../00c5d/00c5d730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d730` · 推定シンボル `None` · 推定型 `None`
- [`00bdae50`](#insn-00bdae50) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae54`](#insn-00bdae54) → [`00bdae60`](#insn-00bdae60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae58`](#insn-00bdae58) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae5c`](#insn-00bdae5c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bdae64`](#insn-00bdae64) → [`00c5da00`](../00c5d/00c5da00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da00` · 推定シンボル `None` · 推定型 `None`
- [`00bdae6c`](#insn-00bdae6c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae74`](#insn-00bdae74) → [`00bdae90`](#insn-00bdae90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae78`](#insn-00bdae78) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae7c`](#insn-00bdae7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae80`](#insn-00bdae80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae84`](#insn-00bdae84) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae90`](#insn-00bdae90) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdadb0`](#insn-00bdadb0)

~~~json
{
  "source": "00bdadb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadb4`](#insn-00bdadb4)

~~~json
{
  "source": "00bdadb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadb8`](#insn-00bdadb8)

~~~json
{
  "source": "00bdadb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadbc`](#insn-00bdadbc)

~~~json
{
  "source": "00bdadbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadd0`](#insn-00bdadd0)

~~~json
{
  "source": "00bdadd0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadd4`](#insn-00bdadd4)

~~~json
{
  "source": "00bdadd4",
  "target": "00bdae2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaddc`](#insn-00bdaddc)

~~~json
{
  "source": "00bdaddc",
  "target": "00c5ae60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdade4`](#insn-00bdade4)

~~~json
{
  "source": "00bdade4",
  "target": "00bdadf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadec`](#insn-00bdadec)

~~~json
{
  "source": "00bdadec",
  "target": "002b2598",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2598",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2598",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdadf0`](#insn-00bdadf0)

~~~json
{
  "source": "00bdadf0",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadf8`](#insn-00bdadf8)

~~~json
{
  "source": "00bdadf8",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae28`](#insn-00bdae28)

~~~json
{
  "source": "00bdae28",
  "target": "00bdae30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae38`](#insn-00bdae38)

~~~json
{
  "source": "00bdae38",
  "target": "00c5d730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae50`](#insn-00bdae50)

~~~json
{
  "source": "00bdae50",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae54`](#insn-00bdae54)

~~~json
{
  "source": "00bdae54",
  "target": "00bdae60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae58`](#insn-00bdae58)

~~~json
{
  "source": "00bdae58",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae5c`](#insn-00bdae5c)

~~~json
{
  "source": "00bdae5c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae64`](#insn-00bdae64)

~~~json
{
  "source": "00bdae64",
  "target": "00c5da00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae6c`](#insn-00bdae6c)

~~~json
{
  "source": "00bdae6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae74`](#insn-00bdae74)

~~~json
{
  "source": "00bdae74",
  "target": "00bdae90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae78`](#insn-00bdae78)

~~~json
{
  "source": "00bdae78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae7c`](#insn-00bdae7c)

~~~json
{
  "source": "00bdae7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae80`](#insn-00bdae80)

~~~json
{
  "source": "00bdae80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae84`](#insn-00bdae84)

~~~json
{
  "source": "00bdae84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae90`](#insn-00bdae90)

~~~json
{
  "source": "00bdae90",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
