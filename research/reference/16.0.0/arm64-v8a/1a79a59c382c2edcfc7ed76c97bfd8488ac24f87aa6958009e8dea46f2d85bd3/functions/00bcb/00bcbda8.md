# 00bcbda8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c8a8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c8a8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-0d85c0f4fbec391f3eafde2f97d0ee7e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc1d0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-207226477963315e245fc9408f853520)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbda8",
  "name": "_ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b77e7c1a59be1bf8940bea89a513b5939272d40c36bba906804eafcd00788ae",
  "source_text_sha256": "5b77e7c1a59be1bf8940bea89a513b5939272d40c36bba906804eafcd00788ae",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbda8",
        "00bcbe1f"
      ]
    ],
    "bytes_sha256": "3ec345585a59aa4ae98fd3af65f4cfff4c85a7a6c0f70511c7ad7a3d8c4f5eb8",
    "instruction_count": 30,
    "instruction_bytes": 120,
    "body_bytes": 120,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5d5a0](../00c5d/00c5d5a0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 823 bytes

~~~c

void _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE(long param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  ulong uVar4;
  
  plVar2 = *(long **)(param_1 + 0x220);
  plVar3 = *(long **)(param_1 + 0x218);
  if (plVar2 != plVar3) {
    uVar4 = 0;
    plVar1 = (long *)*plVar3;
    plVar2 = plVar3;
    while( true ) {
      if (plVar1 != (long *)0x0) {
        (**(code **)(*plVar1 + 8))();
        plVar2 = *(long **)(param_1 + 0x218);
      }
      plVar2[uVar4] = 0;
      plVar2 = *(long **)(param_1 + 0x218);
      uVar4 = uVar4 + 1;
      if ((ulong)(*(long *)(param_1 + 0x220) - (long)plVar2 >> 3) <= uVar4) break;
                    /* catch() { ... } // from try @ 00bcbd90 with catch @ 00bcbdf4 */
      plVar1 = (long *)plVar2[uVar4];
    }
  }
  *(long **)(param_1 + 0x220) = plVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbda8"></a> `00bcbda8` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbdac"></a> `00bcbdac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbdb0"></a> `00bcbdb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbdb4"></a> `00bcbdb4` | `08 10 41 f9` | ldr x8,[x0, #0x220] | `FALL_THROUGH`
<a id="insn-00bcbdb8"></a> `00bcbdb8` | `09 0c 41 f9` | ldr x9,[x0, #0x218] | `FALL_THROUGH`
<a id="insn-00bcbdbc"></a> `00bcbdbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbdc0"></a> `00bcbdc0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbdc4"></a> `00bcbdc4` | `60 02 00 54` | b.eq 0x00bcbe10 | `CONDITIONAL_JUMP`
<a id="insn-00bcbdc8"></a> `00bcbdc8` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bcbdcc"></a> `00bcbdcc` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbdd0"></a> `00bcbdd0` | `00 79 74 f8` | ldr x0,[x8, x20, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bcbdd4"></a> `00bcbdd4` | `40 01 00 b5` | cbnz x0,0x00bcbdfc | `CONDITIONAL_JUMP`
<a id="insn-00bcbdd8"></a> `00bcbdd8` | `1f 79 34 f8` | str xzr,[x8, x20, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bcbddc"></a> `00bcbddc` | `69 12 41 f9` | ldr x9,[x19, #0x220] | `FALL_THROUGH`
<a id="insn-00bcbde0"></a> `00bcbde0` | `68 0e 41 f9` | ldr x8,[x19, #0x218] | `FALL_THROUGH`
<a id="insn-00bcbde4"></a> `00bcbde4` | `94 06 00 91` | add x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbde8"></a> `00bcbde8` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbdec"></a> `00bcbdec` | `9f 0e 89 eb` | cmp x20,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcbdf0"></a> `00bcbdf0` | `02 01 00 54` | b.cs 0x00bcbe10 | `CONDITIONAL_JUMP`
<a id="insn-00bcbdf4"></a> `00bcbdf4` | `00 79 74 f8` | ldr x0,[x8, x20, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bcbdf8"></a> `00bcbdf8` | `00 ff ff b4` | cbz x0,0x00bcbdd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbdfc"></a> `00bcbdfc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbe00"></a> `00bcbe00` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbe04"></a> `00bcbe04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcbe08"></a> `00bcbe08` | `68 0e 41 f9` | ldr x8,[x19, #0x218] | `FALL_THROUGH`
<a id="insn-00bcbe0c"></a> `00bcbe0c` | `f3 ff ff 17` | b 0x00bcbdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbe10"></a> `00bcbe10` | `68 12 01 f9` | str x8,[x19, #0x220] | `FALL_THROUGH`
<a id="insn-00bcbe14"></a> `00bcbe14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe18"></a> `00bcbe18` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbe1c"></a> `00bcbe1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbda8`](#insn-00bcbda8) 範囲 `[['00bcbda8', '00bcbdc7']]`
  - `CONDITIONAL_JUMP` [`00bcbdc4`](#insn-00bcbdc4) → [`00bcbe10`](#insn-00bcbe10)
  - `FALL_THROUGH` [`00bcbdc4`](#insn-00bcbdc4) → [`00bcbdc8`](#insn-00bcbdc8)
- ブロック [`00bcbdc8`](#insn-00bcbdc8) 範囲 `[['00bcbdc8', '00bcbdd7']]`
  - `CONDITIONAL_JUMP` [`00bcbdd4`](#insn-00bcbdd4) → [`00bcbdfc`](#insn-00bcbdfc)
  - `FALL_THROUGH` [`00bcbdd4`](#insn-00bcbdd4) → [`00bcbdd8`](#insn-00bcbdd8)
- ブロック [`00bcbdd8`](#insn-00bcbdd8) 範囲 `[['00bcbdd8', '00bcbdf3']]`
  - `CONDITIONAL_JUMP` [`00bcbdf0`](#insn-00bcbdf0) → [`00bcbe10`](#insn-00bcbe10)
  - `FALL_THROUGH` [`00bcbdf0`](#insn-00bcbdf0) → [`00bcbdf4`](#insn-00bcbdf4)
- ブロック [`00bcbdf4`](#insn-00bcbdf4) 範囲 `[['00bcbdf4', '00bcbdfb']]`
  - `CONDITIONAL_JUMP` [`00bcbdf8`](#insn-00bcbdf8) → [`00bcbdd8`](#insn-00bcbdd8)
  - `FALL_THROUGH` [`00bcbdf8`](#insn-00bcbdf8) → [`00bcbdfc`](#insn-00bcbdfc)
- ブロック [`00bcbdfc`](#insn-00bcbdfc) 範囲 `[['00bcbdfc', '00bcbe0f']]`
  - `UNCONDITIONAL_JUMP` [`00bcbe0c`](#insn-00bcbe0c) → [`00bcbdd8`](#insn-00bcbdd8)
- ブロック [`00bcbe10`](#insn-00bcbe10) 範囲 `[['00bcbe10', '00bcbe1f']]`

## 命令位置別の参照

- [`00bcbda8`](#insn-00bcbda8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdac`](#insn-00bcbdac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdc4`](#insn-00bcbdc4) → [`00bcbe10`](#insn-00bcbe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdd4`](#insn-00bcbdd4) → [`00bcbdfc`](#insn-00bcbdfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdf0`](#insn-00bcbdf0) → [`00bcbe10`](#insn-00bcbe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdf8`](#insn-00bcbdf8) → [`00bcbdd8`](#insn-00bcbdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe0c`](#insn-00bcbe0c) → [`00bcbdd8`](#insn-00bcbdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe14`](#insn-00bcbe14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbda8`](#insn-00bcbda8)

~~~json
{
  "source": "00bcbda8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdac`](#insn-00bcbdac)

~~~json
{
  "source": "00bcbdac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdc4`](#insn-00bcbdc4)

~~~json
{
  "source": "00bcbdc4",
  "target": "00bcbe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdd4`](#insn-00bcbdd4)

~~~json
{
  "source": "00bcbdd4",
  "target": "00bcbdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdf0`](#insn-00bcbdf0)

~~~json
{
  "source": "00bcbdf0",
  "target": "00bcbe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdf8`](#insn-00bcbdf8)

~~~json
{
  "source": "00bcbdf8",
  "target": "00bcbdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe0c`](#insn-00bcbe0c)

~~~json
{
  "source": "00bcbe0c",
  "target": "00bcbdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe14`](#insn-00bcbe14)

~~~json
{
  "source": "00bcbe14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
