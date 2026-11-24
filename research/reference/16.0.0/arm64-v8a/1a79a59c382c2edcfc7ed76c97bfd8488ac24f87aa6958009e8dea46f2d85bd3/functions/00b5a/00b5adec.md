# 00b5adec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afb068`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb068.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-7ea7bcc7573d85cbec553110b1daad33)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b5b214`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b214.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-ea87d37b10d269fff622c4b53141036a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5adec",
  "name": "_ZNK8firebase10LoggerBase8LogDebugEPKcz",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ddfca9e3838fba5a05ddcd922aeaeb2ce8ecec63febe019726dac66f652bdb4",
  "source_text_sha256": "4ddfca9e3838fba5a05ddcd922aeaeb2ce8ecec63febe019726dac66f652bdb4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5adec",
        "00b5aebb"
      ]
    ],
    "bytes_sha256": "a1f50622a8797551a283e04963e8c161589e66c7577be2a5cedfae7842c1e640",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1341 bytes

~~~c

void _ZNK8firebase10LoggerBase8LogDebugEPKcz
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  int iVar2;
  undefined8 local_d0;
  undefined8 uStack_c8;
  undefined8 local_c0;
  undefined8 uStack_b8;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined1 *local_a0;
  undefined1 **ppuStack_98;
  undefined8 *puStack_90;
  undefined8 uStack_88;
  undefined1 *local_60;
  undefined1 **ppuStack_58;
  undefined8 *puStack_50;
  undefined8 uStack_48;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  ppuStack_98 = &local_a0;
  puStack_90 = &local_d0;
  uStack_88 = 0xffffff80ffffffd0;
  local_d0 = param_3;
  uStack_c8 = param_4;
  local_c0 = param_5;
  uStack_b8 = param_6;
  local_b0 = param_7;
  uStack_a8 = param_8;
  local_a0 = (undefined1 *)register0x00000008;
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 < 2) {
    ppuStack_58 = ppuStack_98;
    local_60 = local_a0;
    uStack_48 = uStack_88;
    puStack_50 = puStack_90;
    (**(code **)(*param_1 + 0x20))(param_1,1,param_2,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00b5adec"></a> `00b5adec` | `ff 43 05 d1` | sub sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00b5adf0"></a> `00b5adf0` | `fc 57 12 a9` | stp x28,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00b5adf4"></a> `00b5adf4` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b5adf8"></a> `00b5adf8` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b5adfc"></a> `00b5adfc` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00b5ae00"></a> `00b5ae00` | `e2 0f 08 a9` | stp x2,x3,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b5ae04"></a> `00b5ae04` | `e4 17 09 a9` | stp x4,x5,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b5ae08"></a> `00b5ae08` | `e6 1f 0a a9` | stp x6,x7,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b5ae0c"></a> `00b5ae0c` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00b5ae10"></a> `00b5ae10` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ae14"></a> `00b5ae14` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5ae18"></a> `00b5ae18` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b5ae1c"></a> `00b5ae1c` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b5ae20"></a> `00b5ae20` | `ab 16 40 f9` | ldr x11,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ae24"></a> `00b5ae24` | `e8 03 02 91` | add x8,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b5ae28"></a> `00b5ae28` | `ea 05 80 92` | mov x10,#-0x30 | `FALL_THROUGH`
<a id="insn-00b5ae2c"></a> `00b5ae2c` | `ec 03 00 91` | mov x12,sp | `FALL_THROUGH`
<a id="insn-00b5ae30"></a> `00b5ae30` | `a9 43 00 91` | add x9,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00b5ae34"></a> `00b5ae34` | `0a f0 df f2` | movk x10,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00b5ae38"></a> `00b5ae38` | `08 c1 00 91` | add x8,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00b5ae3c"></a> `00b5ae3c` | `8c 01 02 91` | add x12,x12,#0x80 | `FALL_THROUGH`
<a id="insn-00b5ae40"></a> `00b5ae40` | `ab 83 1d f8` | stur x11,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b5ae44"></a> `00b5ae44` | `a9 23 39 a9` | stp x9,x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00b5ae48"></a> `00b5ae48` | `ac 2b 3a a9` | stp x12,x10,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b5ae4c"></a> `00b5ae4c` | `a1 83 7c ad` | ldp q1,q0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00b5ae50"></a> `00b5ae50` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5ae54"></a> `00b5ae54` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b5ae58"></a> `00b5ae58` | `a1 83 3b ad` | stp q1,q0,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00b5ae5c"></a> `00b5ae5c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5ae60"></a> `00b5ae60` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b5ae64"></a> `00b5ae64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5ae68"></a> `00b5ae68` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b5ae6c"></a> `00b5ae6c` | `4c 01 00 54` | b.gt 0x00b5ae94 | `CONDITIONAL_JUMP`
<a id="insn-00b5ae70"></a> `00b5ae70` | `a0 87 7b ad` | ldp q0,q1,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00b5ae74"></a> `00b5ae74` | `a3 43 01 d1` | sub x3,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b5ae78"></a> `00b5ae78` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00b5ae7c"></a> `00b5ae7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5ae80"></a> `00b5ae80` | `a0 87 3d ad` | stp q0,q1,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b5ae84"></a> `00b5ae84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b5ae88"></a> `00b5ae88` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00b5ae8c"></a> `00b5ae8c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ae90"></a> `00b5ae90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5ae94"></a> `00b5ae94` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ae98"></a> `00b5ae98` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b5ae9c"></a> `00b5ae9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5aea0"></a> `00b5aea0` | `c1 00 00 54` | b.ne 0x00b5aeb8 | `CONDITIONAL_JUMP`
<a id="insn-00b5aea4"></a> `00b5aea4` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b5aea8"></a> `00b5aea8` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b5aeac"></a> `00b5aeac` | `fc 57 52 a9` | ldp x28,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00b5aeb0"></a> `00b5aeb0` | `ff 43 05 91` | add sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00b5aeb4"></a> `00b5aeb4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5aeb8"></a> `00b5aeb8` | `0a f3 03 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5adec`](#insn-00b5adec) 範囲 `[['00b5adec', '00b5ae6f']]`
  - `CONDITIONAL_JUMP` [`00b5ae6c`](#insn-00b5ae6c) → [`00b5ae94`](#insn-00b5ae94)
  - `FALL_THROUGH` [`00b5ae6c`](#insn-00b5ae6c) → [`00b5ae70`](#insn-00b5ae70)
- ブロック [`00b5ae70`](#insn-00b5ae70) 範囲 `[['00b5ae70', '00b5ae93']]`
  - `FALL_THROUGH` [`00b5ae90`](#insn-00b5ae90) → [`00b5ae94`](#insn-00b5ae94)
- ブロック [`00b5ae94`](#insn-00b5ae94) 範囲 `[['00b5ae94', '00b5aea3']]`
  - `CONDITIONAL_JUMP` [`00b5aea0`](#insn-00b5aea0) → [`00b5aeb8`](#insn-00b5aeb8)
  - `FALL_THROUGH` [`00b5aea0`](#insn-00b5aea0) → [`00b5aea4`](#insn-00b5aea4)
- ブロック [`00b5aea4`](#insn-00b5aea4) 範囲 `[['00b5aea4', '00b5aeb7']]`
- ブロック [`00b5aeb8`](#insn-00b5aeb8) 範囲 `[['00b5aeb8', '00b5aebb']]`

## 命令位置別の参照

- [`00b5adf0`](#insn-00b5adf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5adf4`](#insn-00b5adf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5adf8`](#insn-00b5adf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae00`](#insn-00b5ae00) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae04`](#insn-00b5ae04) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae08`](#insn-00b5ae08) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae0c`](#insn-00b5ae0c) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae10`](#insn-00b5ae10) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae14`](#insn-00b5ae14) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae18`](#insn-00b5ae18) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae40`](#insn-00b5ae40) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae44`](#insn-00b5ae44) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae48`](#insn-00b5ae48) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae4c`](#insn-00b5ae4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae58`](#insn-00b5ae58) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae6c`](#insn-00b5ae6c) → [`00b5ae94`](#insn-00b5ae94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae70`](#insn-00b5ae70) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae80`](#insn-00b5ae80) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ae98`](#insn-00b5ae98) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aea0`](#insn-00b5aea0) → [`00b5aeb8`](#insn-00b5aeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aea4`](#insn-00b5aea4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aea8`](#insn-00b5aea8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aeac`](#insn-00b5aeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5aeb8`](#insn-00b5aeb8) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5adf0`](#insn-00b5adf0)

~~~json
{
  "source": "00b5adf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5adf4`](#insn-00b5adf4)

~~~json
{
  "source": "00b5adf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5adf8`](#insn-00b5adf8)

~~~json
{
  "source": "00b5adf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae00`](#insn-00b5ae00)

~~~json
{
  "source": "00b5ae00",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae04`](#insn-00b5ae04)

~~~json
{
  "source": "00b5ae04",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae08`](#insn-00b5ae08)

~~~json
{
  "source": "00b5ae08",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae0c`](#insn-00b5ae0c)

~~~json
{
  "source": "00b5ae0c",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae10`](#insn-00b5ae10)

~~~json
{
  "source": "00b5ae10",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae14`](#insn-00b5ae14)

~~~json
{
  "source": "00b5ae14",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae18`](#insn-00b5ae18)

~~~json
{
  "source": "00b5ae18",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae40`](#insn-00b5ae40)

~~~json
{
  "source": "00b5ae40",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae44`](#insn-00b5ae44)

~~~json
{
  "source": "00b5ae44",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae48`](#insn-00b5ae48)

~~~json
{
  "source": "00b5ae48",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae4c`](#insn-00b5ae4c)

~~~json
{
  "source": "00b5ae4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae58`](#insn-00b5ae58)

~~~json
{
  "source": "00b5ae58",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae6c`](#insn-00b5ae6c)

~~~json
{
  "source": "00b5ae6c",
  "target": "00b5ae94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae70`](#insn-00b5ae70)

~~~json
{
  "source": "00b5ae70",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae80`](#insn-00b5ae80)

~~~json
{
  "source": "00b5ae80",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ae98`](#insn-00b5ae98)

~~~json
{
  "source": "00b5ae98",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aea0`](#insn-00b5aea0)

~~~json
{
  "source": "00b5aea0",
  "target": "00b5aeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aea4`](#insn-00b5aea4)

~~~json
{
  "source": "00b5aea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aea8`](#insn-00b5aea8)

~~~json
{
  "source": "00b5aea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aeac`](#insn-00b5aeac)

~~~json
{
  "source": "00b5aeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5aeb8`](#insn-00b5aeb8)

~~~json
{
  "source": "00b5aeb8",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
