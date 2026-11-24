# 00afe0ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afd0b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afd/00afd0b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0069.md#compare-05975be913e37102f69472a99f3e9e9c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afe0ac",
  "name": "FUN_00afe0ac",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e429987eafec3a27ce5d4a22fdf7ec15b329350b5dbc68a5b6fdb8edc607a29",
  "source_text_sha256": "7e429987eafec3a27ce5d4a22fdf7ec15b329350b5dbc68a5b6fdb8edc607a29",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afe0ac",
        "00afe15f"
      ]
    ],
    "bytes_sha256": "eb0bb87f66650d35cdf661248ceb4392fca6de753882b23d571d3994d1ac7ad1",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1532 bytes

~~~c

void FUN_00afe0ac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  int iVar3;
  
                    /* try { // try from 00afe0bc to 00bfe113 has its CatchHandler @ 00afe0bc
                       catch() { ... } // from try @ 00afe0bc with catch @ 00afe0bc
                       catch() { ... } // from try @ 00afe11c with catch @ 00afe0bc
                       catch() { ... } // from try @ 00afe15c with catch @ 00afe0bc */
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008524fc();
    iVar3 = *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c);
  }
  else {
    iVar3 = 0;
  }
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afe114 to 00bfe11b has its CatchHandler @ 00afe15c */
                    /* try { // try from 00afe11c to 00bfe153 has its CatchHandler @ 00afe0bc */
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008524fc();
    *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c) = iVar3 + param_3;
  }
                    /* try { // try from 00afe154 to 00bfe15b has its CatchHandler @ 00afe15c */
                    /* catch() { ... } // from try @ 00afe114 with catch @ 00afe15c
                       catch() { ... } // from try @ 00afe154 with catch @ 00afe15c
                       try { // try from 00afe15c to 00bfe183 has its CatchHandler @ 00afe0bc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afe0ac"></a> `00afe0ac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afe0b0"></a> `00afe0b0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afe0b4"></a> `00afe0b4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afe0b8"></a> `00afe0b8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afe0bc"></a> `00afe0bc` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afe0c0"></a> `00afe0c0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afe0c4"></a> `00afe0c4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afe0c8"></a> `00afe0c8` | `0d 51 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afe0cc"></a> `00afe0cc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afe0d0"></a> `00afe0d0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afe0d4"></a> `00afe0d4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe0d8"></a> `00afe0d8` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afe0dc"></a> `00afe0dc` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afe0e0"></a> `00afe0e0` | `cc a5 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afe0e4"></a> `00afe0e4` | `40 01 00 37` | tbnz w0,#0x0,0x00afe10c | `CONDITIONAL_JUMP`
<a id="insn-00afe0e8"></a> `00afe0e8` | `05 51 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afe0ec"></a> `00afe0ec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afe0f0"></a> `00afe0f0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afe0f4"></a> `00afe0f4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe0f8"></a> `00afe0f8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afe0fc"></a> `00afe0fc` | `89 49 89 52` | mov w9,#0x4a4c | `FALL_THROUGH`
<a id="insn-00afe100"></a> `00afe100` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe104"></a> `00afe104` | `16 69 69 b8` | ldr w22,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe108"></a> `00afe108` | `02 00 00 14` | b 0x00afe110 | `UNCONDITIONAL_JUMP`
<a id="insn-00afe10c"></a> `00afe10c` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00afe110"></a> `00afe110` | `fb 50 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afe114"></a> `00afe114` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afe118"></a> `00afe118` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afe11c"></a> `00afe11c` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe120"></a> `00afe120` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afe124"></a> `00afe124` | `bb a5 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afe128"></a> `00afe128` | `40 01 00 37` | tbnz w0,#0x0,0x00afe150 | `CONDITIONAL_JUMP`
<a id="insn-00afe12c"></a> `00afe12c` | `d4 02 14 0b` | add w20,w22,w20 | `FALL_THROUGH`
<a id="insn-00afe130"></a> `00afe130` | `f3 50 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afe134"></a> `00afe134` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afe138"></a> `00afe138` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afe13c"></a> `00afe13c` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afe140"></a> `00afe140` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afe144"></a> `00afe144` | `89 49 89 52` | mov w9,#0x4a4c | `FALL_THROUGH`
<a id="insn-00afe148"></a> `00afe148` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afe14c"></a> `00afe14c` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afe150"></a> `00afe150` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afe154"></a> `00afe154` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afe158"></a> `00afe158` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afe15c"></a> `00afe15c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afe0ac`](#insn-00afe0ac) 範囲 `[['00afe0ac', '00afe0bb']]`
  - `FALL_THROUGH` [`00afe0b8`](#insn-00afe0b8) → [`00afe0bc`](#insn-00afe0bc)
- ブロック [`00afe0bc`](#insn-00afe0bc) 範囲 `[['00afe0bc', '00afe0e7']]`
  - `CONDITIONAL_JUMP` [`00afe0e4`](#insn-00afe0e4) → [`00afe10c`](#insn-00afe10c)
  - `FALL_THROUGH` [`00afe0e4`](#insn-00afe0e4) → [`00afe0e8`](#insn-00afe0e8)
- ブロック [`00afe0e8`](#insn-00afe0e8) 範囲 `[['00afe0e8', '00afe10b']]`
  - `UNCONDITIONAL_JUMP` [`00afe108`](#insn-00afe108) → [`00afe110`](#insn-00afe110)
- ブロック [`00afe10c`](#insn-00afe10c) 範囲 `[['00afe10c', '00afe10f']]`
  - `FALL_THROUGH` [`00afe10c`](#insn-00afe10c) → [`00afe110`](#insn-00afe110)
- ブロック [`00afe110`](#insn-00afe110) 範囲 `[['00afe110', '00afe113']]`
  - `FALL_THROUGH` [`00afe110`](#insn-00afe110) → [`00afe114`](#insn-00afe114)
- ブロック [`00afe114`](#insn-00afe114) 範囲 `[['00afe114', '00afe11b']]`
  - `FALL_THROUGH` [`00afe118`](#insn-00afe118) → [`00afe11c`](#insn-00afe11c)
- ブロック [`00afe11c`](#insn-00afe11c) 範囲 `[['00afe11c', '00afe12b']]`
  - `CONDITIONAL_JUMP` [`00afe128`](#insn-00afe128) → [`00afe150`](#insn-00afe150)
  - `FALL_THROUGH` [`00afe128`](#insn-00afe128) → [`00afe12c`](#insn-00afe12c)
- ブロック [`00afe12c`](#insn-00afe12c) 範囲 `[['00afe12c', '00afe14f']]`
  - `FALL_THROUGH` [`00afe14c`](#insn-00afe14c) → [`00afe150`](#insn-00afe150)
- ブロック [`00afe150`](#insn-00afe150) 範囲 `[['00afe150', '00afe153']]`
  - `FALL_THROUGH` [`00afe150`](#insn-00afe150) → [`00afe154`](#insn-00afe154)
- ブロック [`00afe154`](#insn-00afe154) 範囲 `[['00afe154', '00afe15b']]`
  - `FALL_THROUGH` [`00afe158`](#insn-00afe158) → [`00afe15c`](#insn-00afe15c)
- ブロック [`00afe15c`](#insn-00afe15c) 範囲 `[['00afe15c', '00afe15f']]`

## 命令位置別の参照

- [`00afe0ac`](#insn-00afe0ac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe0b0`](#insn-00afe0b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe0b4`](#insn-00afe0b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe0c8`](#insn-00afe0c8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe0e0`](#insn-00afe0e0) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afe0e4`](#insn-00afe0e4) → [`00afe10c`](#insn-00afe10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe0e8`](#insn-00afe0e8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe108`](#insn-00afe108) → [`00afe110`](#insn-00afe110) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe110`](#insn-00afe110) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe124`](#insn-00afe124) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afe128`](#insn-00afe128) → [`00afe150`](#insn-00afe150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe130`](#insn-00afe130) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afe150`](#insn-00afe150) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe154`](#insn-00afe154) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afe158`](#insn-00afe158) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afe0ac`](#insn-00afe0ac)

~~~json
{
  "source": "00afe0ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe0b0`](#insn-00afe0b0)

~~~json
{
  "source": "00afe0b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe0b4`](#insn-00afe0b4)

~~~json
{
  "source": "00afe0b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe0c8`](#insn-00afe0c8)

~~~json
{
  "source": "00afe0c8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe0e0`](#insn-00afe0e0)

~~~json
{
  "source": "00afe0e0",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe0e4`](#insn-00afe0e4)

~~~json
{
  "source": "00afe0e4",
  "target": "00afe10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe0e8`](#insn-00afe0e8)

~~~json
{
  "source": "00afe0e8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe108`](#insn-00afe108)

~~~json
{
  "source": "00afe108",
  "target": "00afe110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe110`](#insn-00afe110)

~~~json
{
  "source": "00afe110",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe124`](#insn-00afe124)

~~~json
{
  "source": "00afe124",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe128`](#insn-00afe128)

~~~json
{
  "source": "00afe128",
  "target": "00afe150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe130`](#insn-00afe130)

~~~json
{
  "source": "00afe130",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afe150`](#insn-00afe150)

~~~json
{
  "source": "00afe150",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe154`](#insn-00afe154)

~~~json
{
  "source": "00afe154",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afe158`](#insn-00afe158)

~~~json
{
  "source": "00afe158",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
