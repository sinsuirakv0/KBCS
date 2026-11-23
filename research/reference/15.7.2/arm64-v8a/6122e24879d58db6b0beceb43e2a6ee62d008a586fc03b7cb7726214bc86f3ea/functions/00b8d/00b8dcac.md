# 00b8dcac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b8dd74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dd74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0076.md#compare-ad34ae6d1b896d2069224b981082de62)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b8dcac",
  "name": "FUN_00b8dcac",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a21d15422cbb595e1bcc6a0a8c43200f8c5f3be2239a94c891dcfd2f82fab144",
  "source_text_sha256": "a21d15422cbb595e1bcc6a0a8c43200f8c5f3be2239a94c891dcfd2f82fab144",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b8dcac",
        "00b8dd5b"
      ]
    ],
    "bytes_sha256": "6c68ea4a9feef9f914c9995eefdf270e3b250fbf0e4e09bad256e5353a227c10",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b8d5b8](../00b8d/00b8d5b8.md)
- [00b90a2c](../00b90/00b90a2c.md)

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1490](../00be1/00be1490.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 970 bytes

~~~c

int FUN_00b8dcac(char *param_1,__locale_t param_2,char *param_3,undefined8 param_4,
                undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  int iVar1;
  __locale_t __dataset;
  undefined1 auStack_a0 [8];
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  
  local_98 = param_4;
  uStack_90 = param_5;
  local_88 = param_6;
  uStack_80 = param_7;
  local_78 = param_8;
  __dataset = uselocale(param_2);
                    /* catch() { ... } // from try @ 00b8dc98 with catch @ 00b8dd24 */
  uStack_58 = 0xffffff80ffffffd8;
  local_70 = (undefined1 *)register0x00000008;
  ppuStack_68 = &local_70;
  puStack_60 = auStack_a0;
  iVar1 = vsscanf(param_1,param_3,&local_70);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b8dcac"></a> `00b8dcac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b8dcb0"></a> `00b8dcb0` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b8dcb4"></a> `00b8dcb4` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b8dcb8"></a> `00b8dcb8` | `fc 57 10 a9` | stp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b8dcbc"></a> `00b8dcbc` | `f4 4f 11 a9` | stp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b8dcc0"></a> `00b8dcc0` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00b8dcc4"></a> `00b8dcc4` | `e8 04 80 92` | mov x8,#-0x28 | `FALL_THROUGH`
<a id="insn-00b8dcc8"></a> `00b8dcc8` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00b8dccc"></a> `00b8dccc` | `aa a3 01 d1` | sub x10,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00b8dcd0"></a> `00b8dcd0` | `08 f0 df f2` | movk x8,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00b8dcd4"></a> `00b8dcd4` | `29 01 02 91` | add x9,x9,#0x80 | `FALL_THROUGH`
<a id="insn-00b8dcd8"></a> `00b8dcd8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b8dcdc"></a> `00b8dcdc` | `a9 23 3f a9` | stp x9,x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00b8dce0"></a> `00b8dce0` | `48 a1 00 91` | add x8,x10,#0x28 | `FALL_THROUGH`
<a id="insn-00b8dce4"></a> `00b8dce4` | `a9 c3 00 91` | add x9,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b8dce8"></a> `00b8dce8` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00b8dcec"></a> `00b8dcec` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00b8dcf0"></a> `00b8dcf0` | `a3 93 39 a9` | stp x3,x4,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00b8dcf4"></a> `00b8dcf4` | `a5 9b 3a a9` | stp x5,x6,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00b8dcf8"></a> `00b8dcf8` | `a7 83 1b f8` | stur x7,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00b8dcfc"></a> `00b8dcfc` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00b8dd00"></a> `00b8dd00` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b8dd04"></a> `00b8dd04` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b8dd08"></a> `00b8dd08` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b8dd0c"></a> `00b8dd0c` | `a9 23 3e a9` | stp x9,x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00b8dd10"></a> `00b8dd10` | `dc 4d 01 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00b8dd14"></a> `00b8dd14` | `a0 07 7f ad` | ldp q0,q1,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00b8dd18"></a> `00b8dd18` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b8dd1c"></a> `00b8dd1c` | `a2 03 01 d1` | sub x2,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00b8dd20"></a> `00b8dd20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b8dd24"></a> `00b8dd24` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00b8dd28"></a> `00b8dd28` | `a0 07 3e ad` | stp q0,q1,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b8dd2c"></a> `00b8dd2c` | `d9 4d 01 94` | bl 0x00be1490 | `UNCONDITIONAL_CALL`
<a id="insn-00b8dd30"></a> `00b8dd30` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00b8dd34"></a> `00b8dd34` | `75 00 00 b4` | cbz x21,0x00b8dd40 | `CONDITIONAL_JUMP`
<a id="insn-00b8dd38"></a> `00b8dd38` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b8dd3c"></a> `00b8dd3c` | `d1 4d 01 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00b8dd40"></a> `00b8dd40` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00b8dd44"></a> `00b8dd44` | `f4 4f 51 a9` | ldp x20,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b8dd48"></a> `00b8dd48` | `fc 57 50 a9` | ldp x28,x21,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b8dd4c"></a> `00b8dd4c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b8dd50"></a> `00b8dd50` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b8dd54"></a> `00b8dd54` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b8dd58"></a> `00b8dd58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b8dcac`](#insn-00b8dcac) 範囲 `[['00b8dcac', '00b8dd23']]`
  - `FALL_THROUGH` [`00b8dd20`](#insn-00b8dd20) → [`00b8dd24`](#insn-00b8dd24)
- ブロック [`00b8dd24`](#insn-00b8dd24) 範囲 `[['00b8dd24', '00b8dd37']]`
  - `CONDITIONAL_JUMP` [`00b8dd34`](#insn-00b8dd34) → [`00b8dd40`](#insn-00b8dd40)
  - `FALL_THROUGH` [`00b8dd34`](#insn-00b8dd34) → [`00b8dd38`](#insn-00b8dd38)
- ブロック [`00b8dd38`](#insn-00b8dd38) 範囲 `[['00b8dd38', '00b8dd3f']]`
  - `FALL_THROUGH` [`00b8dd3c`](#insn-00b8dd3c) → [`00b8dd40`](#insn-00b8dd40)
- ブロック [`00b8dd40`](#insn-00b8dd40) 範囲 `[['00b8dd40', '00b8dd5b']]`

## 命令位置別の参照

- [`00b8dcb4`](#insn-00b8dcb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dcb8`](#insn-00b8dcb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dcbc`](#insn-00b8dcbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dcdc`](#insn-00b8dcdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dcf0`](#insn-00b8dcf0) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dcf4`](#insn-00b8dcf4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dcf8`](#insn-00b8dcf8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dcfc`](#insn-00b8dcfc) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd00`](#insn-00b8dd00) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd04`](#insn-00b8dd04) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd08`](#insn-00b8dd08) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd0c`](#insn-00b8dd0c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd10`](#insn-00b8dd10) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd14`](#insn-00b8dd14) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd28`](#insn-00b8dd28) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd2c`](#insn-00b8dd2c) → [`00be1490`](../00be1/00be1490.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1490` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd34`](#insn-00b8dd34) → [`00b8dd40`](#insn-00b8dd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd3c`](#insn-00b8dd3c) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd44`](#insn-00b8dd44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd48`](#insn-00b8dd48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dd4c`](#insn-00b8dd4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b8dcb4`](#insn-00b8dcb4)

~~~json
{
  "source": "00b8dcb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dcb8`](#insn-00b8dcb8)

~~~json
{
  "source": "00b8dcb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dcbc`](#insn-00b8dcbc)

~~~json
{
  "source": "00b8dcbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dcdc`](#insn-00b8dcdc)

~~~json
{
  "source": "00b8dcdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dcf0`](#insn-00b8dcf0)

~~~json
{
  "source": "00b8dcf0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dcf4`](#insn-00b8dcf4)

~~~json
{
  "source": "00b8dcf4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dcf8`](#insn-00b8dcf8)

~~~json
{
  "source": "00b8dcf8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dcfc`](#insn-00b8dcfc)

~~~json
{
  "source": "00b8dcfc",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd00`](#insn-00b8dd00)

~~~json
{
  "source": "00b8dd00",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd04`](#insn-00b8dd04)

~~~json
{
  "source": "00b8dd04",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd08`](#insn-00b8dd08)

~~~json
{
  "source": "00b8dd08",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd0c`](#insn-00b8dd0c)

~~~json
{
  "source": "00b8dd0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd10`](#insn-00b8dd10)

~~~json
{
  "source": "00b8dd10",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8dd14`](#insn-00b8dd14)

~~~json
{
  "source": "00b8dd14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd28`](#insn-00b8dd28)

~~~json
{
  "source": "00b8dd28",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd2c`](#insn-00b8dd2c)

~~~json
{
  "source": "00b8dd2c",
  "target": "00be1490",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8dd34`](#insn-00b8dd34)

~~~json
{
  "source": "00b8dd34",
  "target": "00b8dd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd3c`](#insn-00b8dd3c)

~~~json
{
  "source": "00b8dd3c",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8dd44`](#insn-00b8dd44)

~~~json
{
  "source": "00b8dd44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd48`](#insn-00b8dd48)

~~~json
{
  "source": "00b8dd48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dd4c`](#insn-00b8dd4c)

~~~json
{
  "source": "00b8dd4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
