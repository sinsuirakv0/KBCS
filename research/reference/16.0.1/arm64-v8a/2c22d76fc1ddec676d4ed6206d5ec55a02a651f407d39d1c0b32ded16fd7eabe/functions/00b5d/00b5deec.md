# 00b5deec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5dac4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dac4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-9c85b1e86f33d973589b272c48d06d3f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5df88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-7ad541359170d1da9bc586cc24894822)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5deec",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_PS0_",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9bfd83e72f7c2defd46b4702b7e7b3ad1c4e32d36160edcdc54aaeddb952065",
  "source_text_sha256": "e9bfd83e72f7c2defd46b4702b7e7b3ad1c4e32d36160edcdc54aaeddb952065",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5deec",
        "00b5dfa3"
      ]
    ],
    "bytes_sha256": "86fe5b439520bc6b010b2dafb42f41a4d380c6bdf447be75e50be2092dafba53",
    "instruction_count": 46,
    "instruction_bytes": 184,
    "body_bytes": 184,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5b0b0](../00c5b/00c5b0b0.md)
- [00c5bbe0](../00c5b/00c5bbe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1124 bytes

~~~c

void _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_
               (undefined8 param_1,undefined8 param_2,byte *param_3)

{
  ulong uVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  byte local_58 [8];
  ulong local_50;
  void *local_48;
  char local_40;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  _ZN8firebase4Path11GetRelativeERKS0_S2_(local_58);
  if (local_40 == '\0') {
    uVar4 = 0;
    goto LAB_00b5df7c;
  }
  if (local_58 == param_3) {
LAB_00b5df5c:
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
    local_40 = '\0';
  }
  else {
    uVar1 = (ulong)(local_58[0] >> 1);
    pvVar3 = (void *)((ulong)local_58 | 1);
    if ((local_58[0] & 1) != 0) {
      uVar1 = local_50;
      pvVar3 = local_48;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_3,pvVar3,uVar1);
    if (local_40 != '\0') goto LAB_00b5df5c;
  }
  uVar4 = 1;
LAB_00b5df7c:
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5deec"></a> `00b5deec` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b5def0"></a> `00b5def0` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5def4"></a> `00b5def4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5def8"></a> `00b5def8` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5defc"></a> `00b5defc` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b5df00"></a> `00b5df00` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b5df04"></a> `00b5df04` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b5df08"></a> `00b5df08` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00b5df0c"></a> `00b5df0c` | `f5 23 00 91` | add x21,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5df10"></a> `00b5df10` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b5df14"></a> `00b5df14` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5df18"></a> `00b5df18` | `32 f7 03 94` | bl 0x00c5bbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5df1c"></a> `00b5df1c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5df20"></a> `00b5df20` | `c8 02 00 34` | cbz w8,0x00b5df78 | `CONDITIONAL_JUMP`
<a id="insn-00b5df24"></a> `00b5df24` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00b5df28"></a> `00b5df28` | `a0 01 00 54` | b.eq 0x00b5df5c | `CONDITIONAL_JUMP`
<a id="insn-00b5df2c"></a> `00b5df2c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b5df30"></a> `00b5df30` | `ea 27 41 a9` | ldp x10,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5df34"></a> `00b5df34` | `eb 23 00 91` | add x11,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b5df38"></a> `00b5df38` | `6b 01 40 b2` | orr x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00b5df3c"></a> `00b5df3c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5df40"></a> `00b5df40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5df44"></a> `00b5df44` | `61 01 89 9a` | csel x1,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00b5df48"></a> `00b5df48` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00b5df4c"></a> `00b5df4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5df50"></a> `00b5df50` | `58 f4 03 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5df54"></a> `00b5df54` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5df58"></a> `00b5df58` | `c8 00 00 34` | cbz w8,0x00b5df70 | `CONDITIONAL_JUMP`
<a id="insn-00b5df5c"></a> `00b5df5c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b5df60"></a> `00b5df60` | `68 00 00 36` | tbz w8,#0x0,0x00b5df6c | `CONDITIONAL_JUMP`
<a id="insn-00b5df64"></a> `00b5df64` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b5df68"></a> `00b5df68` | `d2 e7 03 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5df6c"></a> `00b5df6c` | `ff 83 00 39` | strb wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5df70"></a> `00b5df70` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b5df74"></a> `00b5df74` | `02 00 00 14` | b 0x00b5df7c | `UNCONDITIONAL_JUMP`
<a id="insn-00b5df78"></a> `00b5df78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b5df7c"></a> `00b5df7c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b5df80"></a> `00b5df80` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b5df84"></a> `00b5df84` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5df88"></a> `00b5df88` | `c1 00 00 54` | b.ne 0x00b5dfa0 | `CONDITIONAL_JUMP`
<a id="insn-00b5df8c"></a> `00b5df8c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5df90"></a> `00b5df90` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5df94"></a> `00b5df94` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5df98"></a> `00b5df98` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b5df9c"></a> `00b5df9c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5dfa0"></a> `00b5dfa0` | `d0 e7 03 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5deec`](#insn-00b5deec) 範囲 `[['00b5deec', '00b5df23']]`
  - `CONDITIONAL_JUMP` [`00b5df20`](#insn-00b5df20) → [`00b5df78`](#insn-00b5df78)
  - `FALL_THROUGH` [`00b5df20`](#insn-00b5df20) → [`00b5df24`](#insn-00b5df24)
- ブロック [`00b5df24`](#insn-00b5df24) 範囲 `[['00b5df24', '00b5df2b']]`
  - `CONDITIONAL_JUMP` [`00b5df28`](#insn-00b5df28) → [`00b5df5c`](#insn-00b5df5c)
  - `FALL_THROUGH` [`00b5df28`](#insn-00b5df28) → [`00b5df2c`](#insn-00b5df2c)
- ブロック [`00b5df2c`](#insn-00b5df2c) 範囲 `[['00b5df2c', '00b5df5b']]`
  - `CONDITIONAL_JUMP` [`00b5df58`](#insn-00b5df58) → [`00b5df70`](#insn-00b5df70)
  - `FALL_THROUGH` [`00b5df58`](#insn-00b5df58) → [`00b5df5c`](#insn-00b5df5c)
- ブロック [`00b5df5c`](#insn-00b5df5c) 範囲 `[['00b5df5c', '00b5df63']]`
  - `CONDITIONAL_JUMP` [`00b5df60`](#insn-00b5df60) → [`00b5df6c`](#insn-00b5df6c)
  - `FALL_THROUGH` [`00b5df60`](#insn-00b5df60) → [`00b5df64`](#insn-00b5df64)
- ブロック [`00b5df64`](#insn-00b5df64) 範囲 `[['00b5df64', '00b5df6b']]`
  - `FALL_THROUGH` [`00b5df68`](#insn-00b5df68) → [`00b5df6c`](#insn-00b5df6c)
- ブロック [`00b5df6c`](#insn-00b5df6c) 範囲 `[['00b5df6c', '00b5df6f']]`
  - `FALL_THROUGH` [`00b5df6c`](#insn-00b5df6c) → [`00b5df70`](#insn-00b5df70)
- ブロック [`00b5df70`](#insn-00b5df70) 範囲 `[['00b5df70', '00b5df77']]`
  - `UNCONDITIONAL_JUMP` [`00b5df74`](#insn-00b5df74) → [`00b5df7c`](#insn-00b5df7c)
- ブロック [`00b5df78`](#insn-00b5df78) 範囲 `[['00b5df78', '00b5df7b']]`
  - `FALL_THROUGH` [`00b5df78`](#insn-00b5df78) → [`00b5df7c`](#insn-00b5df7c)
- ブロック [`00b5df7c`](#insn-00b5df7c) 範囲 `[['00b5df7c', '00b5df8b']]`
  - `CONDITIONAL_JUMP` [`00b5df88`](#insn-00b5df88) → [`00b5dfa0`](#insn-00b5dfa0)
  - `FALL_THROUGH` [`00b5df88`](#insn-00b5df88) → [`00b5df8c`](#insn-00b5df8c)
- ブロック [`00b5df8c`](#insn-00b5df8c) 範囲 `[['00b5df8c', '00b5df9f']]`
- ブロック [`00b5dfa0`](#insn-00b5dfa0) 範囲 `[['00b5dfa0', '00b5dfa3']]`

## 命令位置別の参照

- [`00b5def0`](#insn-00b5def0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5def4`](#insn-00b5def4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5def8`](#insn-00b5def8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df10`](#insn-00b5df10) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df18`](#insn-00b5df18) → [`00c5bbe0`](../00c5b/00c5bbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bbe0` · 推定シンボル `None` · 推定型 `None`
- [`00b5df1c`](#insn-00b5df1c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df20`](#insn-00b5df20) → [`00b5df78`](#insn-00b5df78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df28`](#insn-00b5df28) → [`00b5df5c`](#insn-00b5df5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df2c`](#insn-00b5df2c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df30`](#insn-00b5df30) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df50`](#insn-00b5df50) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b5df54`](#insn-00b5df54) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df58`](#insn-00b5df58) → [`00b5df70`](#insn-00b5df70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df5c`](#insn-00b5df5c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df60`](#insn-00b5df60) → [`00b5df6c`](#insn-00b5df6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df64`](#insn-00b5df64) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df68`](#insn-00b5df68) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b5df6c`](#insn-00b5df6c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df74`](#insn-00b5df74) → [`00b5df7c`](#insn-00b5df7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df80`](#insn-00b5df80) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df88`](#insn-00b5df88) → [`00b5dfa0`](#insn-00b5dfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df8c`](#insn-00b5df8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df90`](#insn-00b5df90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5df94`](#insn-00b5df94) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5dfa0`](#insn-00b5dfa0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5def0`](#insn-00b5def0)

~~~json
{
  "source": "00b5def0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5def4`](#insn-00b5def4)

~~~json
{
  "source": "00b5def4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5def8`](#insn-00b5def8)

~~~json
{
  "source": "00b5def8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df10`](#insn-00b5df10)

~~~json
{
  "source": "00b5df10",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df18`](#insn-00b5df18)

~~~json
{
  "source": "00b5df18",
  "target": "00c5bbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5df1c`](#insn-00b5df1c)

~~~json
{
  "source": "00b5df1c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df20`](#insn-00b5df20)

~~~json
{
  "source": "00b5df20",
  "target": "00b5df78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df28`](#insn-00b5df28)

~~~json
{
  "source": "00b5df28",
  "target": "00b5df5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df2c`](#insn-00b5df2c)

~~~json
{
  "source": "00b5df2c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df30`](#insn-00b5df30)

~~~json
{
  "source": "00b5df30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df50`](#insn-00b5df50)

~~~json
{
  "source": "00b5df50",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5df54`](#insn-00b5df54)

~~~json
{
  "source": "00b5df54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df58`](#insn-00b5df58)

~~~json
{
  "source": "00b5df58",
  "target": "00b5df70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df5c`](#insn-00b5df5c)

~~~json
{
  "source": "00b5df5c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df60`](#insn-00b5df60)

~~~json
{
  "source": "00b5df60",
  "target": "00b5df6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df64`](#insn-00b5df64)

~~~json
{
  "source": "00b5df64",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df68`](#insn-00b5df68)

~~~json
{
  "source": "00b5df68",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5df6c`](#insn-00b5df6c)

~~~json
{
  "source": "00b5df6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df74`](#insn-00b5df74)

~~~json
{
  "source": "00b5df74",
  "target": "00b5df7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df80`](#insn-00b5df80)

~~~json
{
  "source": "00b5df80",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df88`](#insn-00b5df88)

~~~json
{
  "source": "00b5df88",
  "target": "00b5dfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df8c`](#insn-00b5df8c)

~~~json
{
  "source": "00b5df8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df90`](#insn-00b5df90)

~~~json
{
  "source": "00b5df90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5df94`](#insn-00b5df94)

~~~json
{
  "source": "00b5df94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5dfa0`](#insn-00b5dfa0)

~~~json
{
  "source": "00b5dfa0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
