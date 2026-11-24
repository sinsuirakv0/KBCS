# 00a9abfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a9aa00`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9aa00.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0062.md#compare-856a36642c8c0fb83b24c486cb3af653)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a9ac6c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9a/00a9ac6c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0063.md#compare-a718dde6244796f044403e4c77084143)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9abfc",
  "name": "FUN_00a9abfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4db44faee9d081d6491b08e645ac53bb10e2710c51effcdcfba00669af7ce3e5",
  "source_text_sha256": "4db44faee9d081d6491b08e645ac53bb10e2710c51effcdcfba00669af7ce3e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9abfc",
        "00a9ac77"
      ]
    ],
    "bytes_sha256": "04716ab97d7e9cb939d618f492f0b56125fecc0b28fe44da2bee7e8f8dcd281d",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00764ee0](../00764/00764ee0.md)
- [008514f8](../00851/008514f8.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 574 bytes

~~~c

void FUN_00a9abfc(void)

{
  long lVar1;
  long lVar2;
  byte local_40 [8];
  ulong local_38;
  void *pvStack_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_008514f8();
  FUN_00764ee0(local_40);
  if ((local_40[0] & 1) == 0) {
    local_38 = (ulong)(local_40[0] >> 1);
  }
  else {
    _ZdlPv(pvStack_30);
  }
  lVar2 = FUN_008514f8();
  *(bool *)(lVar2 + 0x44e37a) = local_38 == 0;
  if (*(long *)(lVar1 + 0x28) == local_28) {
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
<a id="insn-00a9abfc"></a> `00a9abfc` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00a9ac00"></a> `00a9ac00` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ac04"></a> `00a9ac04` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9ac08"></a> `00a9ac08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a9ac0c"></a> `00a9ac0c` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a9ac10"></a> `00a9ac10` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00a9ac14"></a> `00a9ac14` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9ac18"></a> `00a9ac18` | `38 da f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac1c"></a> `00a9ac1c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a9ac20"></a> `00a9ac20` | `b0 28 f3 97` | bl 0x00764ee0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac24"></a> `00a9ac24` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a9ac28"></a> `00a9ac28` | `68 00 00 37` | tbnz w8,#0x0,0x00a9ac34 | `CONDITIONAL_JUMP`
<a id="insn-00a9ac2c"></a> `00a9ac2c` | `14 fd 41 d3` | lsr x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a9ac30"></a> `00a9ac30` | `03 00 00 14` | b 0x00a9ac3c | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ac34"></a> `00a9ac34` | `f4 83 40 a9` | ldp x20,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a9ac38"></a> `00a9ac38` | `9e f4 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac3c"></a> `00a9ac3c` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00a9ac40"></a> `00a9ac40` | `f4 17 9f 1a` | cset w20,eq | `FALL_THROUGH`
<a id="insn-00a9ac44"></a> `00a9ac44` | `2d da f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac48"></a> `00a9ac48` | `48 6f 9c 52` | mov w8,#0xe37a | `FALL_THROUGH`
<a id="insn-00a9ac4c"></a> `00a9ac4c` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ac50"></a> `00a9ac50` | `14 68 28 38` | strb w20,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a9ac54"></a> `00a9ac54` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00a9ac58"></a> `00a9ac58` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9ac5c"></a> `00a9ac5c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a9ac60"></a> `00a9ac60` | `a1 00 00 54` | b.ne 0x00a9ac74 | `CONDITIONAL_JUMP`
<a id="insn-00a9ac64"></a> `00a9ac64` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9ac68"></a> `00a9ac68` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ac6c"></a> `00a9ac6c` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00a9ac70"></a> `00a9ac70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a9ac74"></a> `00a9ac74` | `9b f4 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9abfc`](#insn-00a9abfc) 範囲 `[['00a9abfc', '00a9ac2b']]`
  - `CONDITIONAL_JUMP` [`00a9ac28`](#insn-00a9ac28) → [`00a9ac34`](#insn-00a9ac34)
  - `FALL_THROUGH` [`00a9ac28`](#insn-00a9ac28) → [`00a9ac2c`](#insn-00a9ac2c)
- ブロック [`00a9ac2c`](#insn-00a9ac2c) 範囲 `[['00a9ac2c', '00a9ac33']]`
  - `UNCONDITIONAL_JUMP` [`00a9ac30`](#insn-00a9ac30) → [`00a9ac3c`](#insn-00a9ac3c)
- ブロック [`00a9ac34`](#insn-00a9ac34) 範囲 `[['00a9ac34', '00a9ac3b']]`
  - `FALL_THROUGH` [`00a9ac38`](#insn-00a9ac38) → [`00a9ac3c`](#insn-00a9ac3c)
- ブロック [`00a9ac3c`](#insn-00a9ac3c) 範囲 `[['00a9ac3c', '00a9ac63']]`
  - `CONDITIONAL_JUMP` [`00a9ac60`](#insn-00a9ac60) → [`00a9ac74`](#insn-00a9ac74)
  - `FALL_THROUGH` [`00a9ac60`](#insn-00a9ac60) → [`00a9ac64`](#insn-00a9ac64)
- ブロック [`00a9ac64`](#insn-00a9ac64) 範囲 `[['00a9ac64', '00a9ac73']]`
- ブロック [`00a9ac74`](#insn-00a9ac74) 範囲 `[['00a9ac74', '00a9ac77']]`

## 命令位置別の参照

- [`00a9ac00`](#insn-00a9ac00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac04`](#insn-00a9ac04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac14`](#insn-00a9ac14) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac18`](#insn-00a9ac18) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac20`](#insn-00a9ac20) → [`00764ee0`](../00764/00764ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00764ee0` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac24`](#insn-00a9ac24) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac28`](#insn-00a9ac28) → [`00a9ac34`](#insn-00a9ac34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac30`](#insn-00a9ac30) → [`00a9ac3c`](#insn-00a9ac3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac34`](#insn-00a9ac34) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac38`](#insn-00a9ac38) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac44`](#insn-00a9ac44) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac58`](#insn-00a9ac58) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac60`](#insn-00a9ac60) → [`00a9ac74`](#insn-00a9ac74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac64`](#insn-00a9ac64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac68`](#insn-00a9ac68) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac74`](#insn-00a9ac74) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9ac00`](#insn-00a9ac00)

~~~json
{
  "source": "00a9ac00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac04`](#insn-00a9ac04)

~~~json
{
  "source": "00a9ac04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac14`](#insn-00a9ac14)

~~~json
{
  "source": "00a9ac14",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac18`](#insn-00a9ac18)

~~~json
{
  "source": "00a9ac18",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac20`](#insn-00a9ac20)

~~~json
{
  "source": "00a9ac20",
  "target": "00764ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac24`](#insn-00a9ac24)

~~~json
{
  "source": "00a9ac24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac28`](#insn-00a9ac28)

~~~json
{
  "source": "00a9ac28",
  "target": "00a9ac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac30`](#insn-00a9ac30)

~~~json
{
  "source": "00a9ac30",
  "target": "00a9ac3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac34`](#insn-00a9ac34)

~~~json
{
  "source": "00a9ac34",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac38`](#insn-00a9ac38)

~~~json
{
  "source": "00a9ac38",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac44`](#insn-00a9ac44)

~~~json
{
  "source": "00a9ac44",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac58`](#insn-00a9ac58)

~~~json
{
  "source": "00a9ac58",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac60`](#insn-00a9ac60)

~~~json
{
  "source": "00a9ac60",
  "target": "00a9ac74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac64`](#insn-00a9ac64)

~~~json
{
  "source": "00a9ac64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac68`](#insn-00a9ac68)

~~~json
{
  "source": "00a9ac68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac74`](#insn-00a9ac74)

~~~json
{
  "source": "00a9ac74",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
