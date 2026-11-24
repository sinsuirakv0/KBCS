# 00abd8dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abd86c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd86c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0005.md#compare-0512ce042dcad342c558a5a3c3dfe599)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00abe8d0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00abe/00abe8d0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0011.md#compare-1e973a145d8c7ccae56db2f7bbcec208)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abd8dc",
  "name": "FUN_00abd8dc",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4919b99bf919285e2ca2760a2df4a3b319bf8d1f3af141088d37c3628866f8fc",
  "source_text_sha256": "4919b99bf919285e2ca2760a2df4a3b319bf8d1f3af141088d37c3628866f8fc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abd8dc",
        "00abd95b"
      ]
    ],
    "bytes_sha256": "3eb8cade4e11e9c772a764763eda8875654fd18e08a750ea7918806818811a2d",
    "instruction_count": 32,
    "instruction_bytes": 128,
    "body_bytes": 128,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0086a244](../0086a/0086a244.md)
- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 615 bytes

~~~c

void FUN_00abd8dc(undefined8 *param_1)

{
  long *__ptr;
  long lVar1;
  long *plVar2;
  long *plVar3;
  
                    /* try { // try from 00abd8e4 to 00bbd963 has its CatchHandler @ 00abd840 */
  plVar3 = (long *)*param_1;
  if (plVar3 == (long *)0x0) {
    return;
  }
  plVar2 = (long *)param_1[1];
  __ptr = plVar3;
  if (plVar2 != plVar3) {
    do {
      plVar2 = plVar2 + -1;
      lVar1 = *plVar2;
      *plVar2 = 0;
      if (lVar1 != 0) {
        FUN_0086a244(plVar2);
      }
    } while (plVar2 != plVar3);
    __ptr = (long *)*param_1;
  }
  param_1[1] = plVar3;
  _ZdlPv(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abd8dc"></a> `00abd8dc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00abd8e0"></a> `00abd8e0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd8e4"></a> `00abd8e4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd8e8"></a> `00abd8e8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abd8ec"></a> `00abd8ec` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-00abd8f0"></a> `00abd8f0` | `f5 02 00 b4` | cbz x21,0x00abd94c | `CONDITIONAL_JUMP`
<a id="insn-00abd8f4"></a> `00abd8f4` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00abd8f8"></a> `00abd8f8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abd8fc"></a> `00abd8fc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abd900"></a> `00abd900` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00abd904"></a> `00abd904` | `a0 01 00 54` | b.eq 0x00abd938 | `CONDITIONAL_JUMP`
<a id="insn-00abd908"></a> `00abd908` | `14 21 00 d1` | sub x20,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00abd90c"></a> `00abd90c` | `04 00 00 14` | b 0x00abd91c | `UNCONDITIONAL_JUMP`
<a id="insn-00abd910"></a> `00abd910` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-00abd914"></a> `00abd914` | `94 22 00 d1` | sub x20,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abd918"></a> `00abd918` | `e0 00 00 54` | b.eq 0x00abd934 | `CONDITIONAL_JUMP`
<a id="insn-00abd91c"></a> `00abd91c` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00abd920"></a> `00abd920` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00abd924"></a> `00abd924` | `61 ff ff b4` | cbz x1,0x00abd910 | `CONDITIONAL_JUMP`
<a id="insn-00abd928"></a> `00abd928` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abd92c"></a> `00abd92c` | `46 b2 f6 97` | bl 0x0086a244 | `UNCONDITIONAL_CALL`
<a id="insn-00abd930"></a> `00abd930` | `f8 ff ff 17` | b 0x00abd910 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd934"></a> `00abd934` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00abd938"></a> `00abd938` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abd93c"></a> `00abd93c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd940"></a> `00abd940` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd944"></a> `00abd944` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00abd948"></a> `00abd948` | `8e 69 06 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00abd94c"></a> `00abd94c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd950"></a> `00abd950` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd954"></a> `00abd954` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00abd958"></a> `00abd958` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abd8dc`](#insn-00abd8dc) 範囲 `[['00abd8dc', '00abd8e3']]`
  - `FALL_THROUGH` [`00abd8e0`](#insn-00abd8e0) → [`00abd8e4`](#insn-00abd8e4)
- ブロック [`00abd8e4`](#insn-00abd8e4) 範囲 `[['00abd8e4', '00abd8f3']]`
  - `CONDITIONAL_JUMP` [`00abd8f0`](#insn-00abd8f0) → [`00abd94c`](#insn-00abd94c)
  - `FALL_THROUGH` [`00abd8f0`](#insn-00abd8f0) → [`00abd8f4`](#insn-00abd8f4)
- ブロック [`00abd8f4`](#insn-00abd8f4) 範囲 `[['00abd8f4', '00abd907']]`
  - `CONDITIONAL_JUMP` [`00abd904`](#insn-00abd904) → [`00abd938`](#insn-00abd938)
  - `FALL_THROUGH` [`00abd904`](#insn-00abd904) → [`00abd908`](#insn-00abd908)
- ブロック [`00abd908`](#insn-00abd908) 範囲 `[['00abd908', '00abd90f']]`
  - `UNCONDITIONAL_JUMP` [`00abd90c`](#insn-00abd90c) → [`00abd91c`](#insn-00abd91c)
- ブロック [`00abd910`](#insn-00abd910) 範囲 `[['00abd910', '00abd91b']]`
  - `CONDITIONAL_JUMP` [`00abd918`](#insn-00abd918) → [`00abd934`](#insn-00abd934)
  - `FALL_THROUGH` [`00abd918`](#insn-00abd918) → [`00abd91c`](#insn-00abd91c)
- ブロック [`00abd91c`](#insn-00abd91c) 範囲 `[['00abd91c', '00abd927']]`
  - `CONDITIONAL_JUMP` [`00abd924`](#insn-00abd924) → [`00abd910`](#insn-00abd910)
  - `FALL_THROUGH` [`00abd924`](#insn-00abd924) → [`00abd928`](#insn-00abd928)
- ブロック [`00abd928`](#insn-00abd928) 範囲 `[['00abd928', '00abd933']]`
  - `UNCONDITIONAL_JUMP` [`00abd930`](#insn-00abd930) → [`00abd910`](#insn-00abd910)
- ブロック [`00abd934`](#insn-00abd934) 範囲 `[['00abd934', '00abd937']]`
  - `FALL_THROUGH` [`00abd934`](#insn-00abd934) → [`00abd938`](#insn-00abd938)
- ブロック [`00abd938`](#insn-00abd938) 範囲 `[['00abd938', '00abd94b']]`
- ブロック [`00abd94c`](#insn-00abd94c) 範囲 `[['00abd94c', '00abd95b']]`

## 命令位置別の参照

- [`00abd8dc`](#insn-00abd8dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd8e0`](#insn-00abd8e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd8e4`](#insn-00abd8e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd8f0`](#insn-00abd8f0) → [`00abd94c`](#insn-00abd94c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd904`](#insn-00abd904) → [`00abd938`](#insn-00abd938) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd90c`](#insn-00abd90c) → [`00abd91c`](#insn-00abd91c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd918`](#insn-00abd918) → [`00abd934`](#insn-00abd934) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd924`](#insn-00abd924) → [`00abd910`](#insn-00abd910) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd92c`](#insn-00abd92c) → [`0086a244`](../0086a/0086a244.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086a244` · 推定シンボル `None` · 推定型 `None`
- [`00abd930`](#insn-00abd930) → [`00abd910`](#insn-00abd910) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd93c`](#insn-00abd93c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd940`](#insn-00abd940) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd944`](#insn-00abd944) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd948`](#insn-00abd948) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00abd94c`](#insn-00abd94c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd950`](#insn-00abd950) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd954`](#insn-00abd954) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abd8dc`](#insn-00abd8dc)

~~~json
{
  "source": "00abd8dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd8e0`](#insn-00abd8e0)

~~~json
{
  "source": "00abd8e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd8e4`](#insn-00abd8e4)

~~~json
{
  "source": "00abd8e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd8f0`](#insn-00abd8f0)

~~~json
{
  "source": "00abd8f0",
  "target": "00abd94c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd904`](#insn-00abd904)

~~~json
{
  "source": "00abd904",
  "target": "00abd938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd90c`](#insn-00abd90c)

~~~json
{
  "source": "00abd90c",
  "target": "00abd91c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd918`](#insn-00abd918)

~~~json
{
  "source": "00abd918",
  "target": "00abd934",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd924`](#insn-00abd924)

~~~json
{
  "source": "00abd924",
  "target": "00abd910",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd92c`](#insn-00abd92c)

~~~json
{
  "source": "00abd92c",
  "target": "0086a244",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd930`](#insn-00abd930)

~~~json
{
  "source": "00abd930",
  "target": "00abd910",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd93c`](#insn-00abd93c)

~~~json
{
  "source": "00abd93c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd940`](#insn-00abd940)

~~~json
{
  "source": "00abd940",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd944`](#insn-00abd944)

~~~json
{
  "source": "00abd944",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd948`](#insn-00abd948)

~~~json
{
  "source": "00abd948",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd94c`](#insn-00abd94c)

~~~json
{
  "source": "00abd94c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd950`](#insn-00abd950)

~~~json
{
  "source": "00abd950",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd954`](#insn-00abd954)

~~~json
{
  "source": "00abd954",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
