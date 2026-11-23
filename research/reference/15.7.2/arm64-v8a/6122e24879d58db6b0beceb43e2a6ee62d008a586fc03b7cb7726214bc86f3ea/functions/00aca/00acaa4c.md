# 00acaa4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acab14`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aca/00acab14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-d351b1f679615dec29034ccd10dae4ff)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaa4c",
  "name": "FUN_00acaa4c",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64e42402d3fce5d38b79094d3adacec480a48dd0c23114704866fd103801921e",
  "source_text_sha256": "64e42402d3fce5d38b79094d3adacec480a48dd0c23114704866fd103801921e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acaa4c",
        "00acaaeb"
      ]
    ],
    "bytes_sha256": "17699334ec91bcc471f1616fc582ac1ff15a86ecfe308ab7449badf98a866d42",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 858 bytes

~~~c

void FUN_00acaa4c(undefined8 *param_1)

{
  long lVar1;
  void *__ptr;
  long lVar2;
  
  lVar1 = param_1[1];
  lVar2 = param_1[2];
  do {
    if (lVar2 == lVar1) {
      if ((void *)*param_1 != (void *)0x0) {
        _ZdlPv((void *)*param_1);
        return;
      }
      return;
    }
    param_1[2] = lVar2 + -0x60;
    if ((*(byte *)(lVar2 + -0x18) & 1) == 0) {
      if ((*(byte *)(lVar2 + -0x30) & 1) == 0) goto LAB_00acaa8c;
LAB_00acaaa8:
      _ZdlPv(*(void **)(lVar2 + -0x20));
      __ptr = *(void **)(lVar2 + -0x48);
    }
    else {
      _ZdlPv(*(void **)(lVar2 + -8));
      if ((*(byte *)(lVar2 + -0x30) & 1) != 0) goto LAB_00acaaa8;
LAB_00acaa8c:
      __ptr = *(void **)(lVar2 + -0x48);
    }
    if (__ptr != (void *)0x0) {
      *(void **)(lVar2 + -0x40) = __ptr;
      _ZdlPv(__ptr);
    }
    lVar2 = param_1[2];
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acaa4c"></a> `00acaa4c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acaa50"></a> `00acaa50` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acaa54"></a> `00acaa54` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acaa58"></a> `00acaa58` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acaa5c"></a> `00acaa5c` | `14 d4 40 a9` | ldp x20,x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acaa60"></a> `00acaa60` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acaa64"></a> `00acaa64` | `02 00 00 14` | b 0x00acaa6c | `UNCONDITIONAL_JUMP`
<a id="insn-00acaa68"></a> `00acaa68` | `75 0a 40 f9` | ldr x21,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acaa6c"></a> `00acaa6c` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00acaa70"></a> `00acaa70` | `a0 02 00 54` | b.eq 0x00acaac4 | `CONDITIONAL_JUMP`
<a id="insn-00acaa74"></a> `00acaa74` | `a8 82 01 d1` | sub x8,x21,#0x60 | `FALL_THROUGH`
<a id="insn-00acaa78"></a> `00acaa78` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acaa7c"></a> `00acaa7c` | `a8 82 5e 38` | ldurb w8,[x21, #-0x18] | `FALL_THROUGH`
<a id="insn-00acaa80"></a> `00acaa80` | `c8 00 00 37` | tbnz w8,#0x0,0x00acaa98 | `CONDITIONAL_JUMP`
<a id="insn-00acaa84"></a> `00acaa84` | `a8 02 5d 38` | ldurb w8,[x21, #-0x30] | `FALL_THROUGH`
<a id="insn-00acaa88"></a> `00acaa88` | `08 01 00 37` | tbnz w8,#0x0,0x00acaaa8 | `CONDITIONAL_JUMP`
<a id="insn-00acaa8c"></a> `00acaa8c` | `a0 82 5b f8` | ldur x0,[x21, #-0x48] | `FALL_THROUGH`
<a id="insn-00acaa90"></a> `00acaa90` | `40 01 00 b5` | cbnz x0,0x00acaab8 | `CONDITIONAL_JUMP`
<a id="insn-00acaa94"></a> `00acaa94` | `f5 ff ff 17` | b 0x00acaa68 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaa98"></a> `00acaa98` | `a0 82 5f f8` | ldur x0,[x21, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaa9c"></a> `00acaa9c` | `31 41 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acaaa0"></a> `00acaaa0` | `a8 02 5d 38` | ldurb w8,[x21, #-0x30] | `FALL_THROUGH`
<a id="insn-00acaaa4"></a> `00acaaa4` | `48 ff 07 36` | tbz w8,#0x0,0x00acaa8c | `CONDITIONAL_JUMP`
<a id="insn-00acaaa8"></a> `00acaaa8` | `a0 02 5e f8` | ldur x0,[x21, #-0x20] | `FALL_THROUGH`
<a id="insn-00acaaac"></a> `00acaaac` | `2d 41 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acaab0"></a> `00acaab0` | `a0 82 5b f8` | ldur x0,[x21, #-0x48] | `FALL_THROUGH`
<a id="insn-00acaab4"></a> `00acaab4` | `a0 fd ff b4` | cbz x0,0x00acaa68 | `CONDITIONAL_JUMP`
<a id="insn-00acaab8"></a> `00acaab8` | `a0 02 1c f8` | stur x0,[x21, #-0x40] | `FALL_THROUGH`
<a id="insn-00acaabc"></a> `00acaabc` | `29 41 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acaac0"></a> `00acaac0` | `ea ff ff 17` | b 0x00acaa68 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaac4"></a> `00acaac4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00acaac8"></a> `00acaac8` | `a0 00 00 b4` | cbz x0,0x00acaadc | `CONDITIONAL_JUMP`
<a id="insn-00acaacc"></a> `00acaacc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acaad0"></a> `00acaad0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acaad4"></a> `00acaad4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acaad8"></a> `00acaad8` | `22 41 04 14` | b 0x00bdaf60 | `CALL_TERMINATOR`
<a id="insn-00acaadc"></a> `00acaadc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acaae0"></a> `00acaae0` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acaae4"></a> `00acaae4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acaae8"></a> `00acaae8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acaa4c`](#insn-00acaa4c) 範囲 `[['00acaa4c', '00acaa67']]`
  - `UNCONDITIONAL_JUMP` [`00acaa64`](#insn-00acaa64) → [`00acaa6c`](#insn-00acaa6c)
- ブロック [`00acaa68`](#insn-00acaa68) 範囲 `[['00acaa68', '00acaa6b']]`
  - `FALL_THROUGH` [`00acaa68`](#insn-00acaa68) → [`00acaa6c`](#insn-00acaa6c)
- ブロック [`00acaa6c`](#insn-00acaa6c) 範囲 `[['00acaa6c', '00acaa73']]`
  - `CONDITIONAL_JUMP` [`00acaa70`](#insn-00acaa70) → [`00acaac4`](#insn-00acaac4)
  - `FALL_THROUGH` [`00acaa70`](#insn-00acaa70) → [`00acaa74`](#insn-00acaa74)
- ブロック [`00acaa74`](#insn-00acaa74) 範囲 `[['00acaa74', '00acaa83']]`
  - `CONDITIONAL_JUMP` [`00acaa80`](#insn-00acaa80) → [`00acaa98`](#insn-00acaa98)
  - `FALL_THROUGH` [`00acaa80`](#insn-00acaa80) → [`00acaa84`](#insn-00acaa84)
- ブロック [`00acaa84`](#insn-00acaa84) 範囲 `[['00acaa84', '00acaa8b']]`
  - `CONDITIONAL_JUMP` [`00acaa88`](#insn-00acaa88) → [`00acaaa8`](#insn-00acaaa8)
  - `FALL_THROUGH` [`00acaa88`](#insn-00acaa88) → [`00acaa8c`](#insn-00acaa8c)
- ブロック [`00acaa8c`](#insn-00acaa8c) 範囲 `[['00acaa8c', '00acaa93']]`
  - `CONDITIONAL_JUMP` [`00acaa90`](#insn-00acaa90) → [`00acaab8`](#insn-00acaab8)
  - `FALL_THROUGH` [`00acaa90`](#insn-00acaa90) → [`00acaa94`](#insn-00acaa94)
- ブロック [`00acaa94`](#insn-00acaa94) 範囲 `[['00acaa94', '00acaa97']]`
  - `UNCONDITIONAL_JUMP` [`00acaa94`](#insn-00acaa94) → [`00acaa68`](#insn-00acaa68)
- ブロック [`00acaa98`](#insn-00acaa98) 範囲 `[['00acaa98', '00acaaa7']]`
  - `CONDITIONAL_JUMP` [`00acaaa4`](#insn-00acaaa4) → [`00acaa8c`](#insn-00acaa8c)
  - `FALL_THROUGH` [`00acaaa4`](#insn-00acaaa4) → [`00acaaa8`](#insn-00acaaa8)
- ブロック [`00acaaa8`](#insn-00acaaa8) 範囲 `[['00acaaa8', '00acaab7']]`
  - `CONDITIONAL_JUMP` [`00acaab4`](#insn-00acaab4) → [`00acaa68`](#insn-00acaa68)
  - `FALL_THROUGH` [`00acaab4`](#insn-00acaab4) → [`00acaab8`](#insn-00acaab8)
- ブロック [`00acaab8`](#insn-00acaab8) 範囲 `[['00acaab8', '00acaac3']]`
  - `UNCONDITIONAL_JUMP` [`00acaac0`](#insn-00acaac0) → [`00acaa68`](#insn-00acaa68)
- ブロック [`00acaac4`](#insn-00acaac4) 範囲 `[['00acaac4', '00acaacb']]`
  - `CONDITIONAL_JUMP` [`00acaac8`](#insn-00acaac8) → [`00acaadc`](#insn-00acaadc)
  - `FALL_THROUGH` [`00acaac8`](#insn-00acaac8) → [`00acaacc`](#insn-00acaacc)
- ブロック [`00acaacc`](#insn-00acaacc) 範囲 `[['00acaacc', '00acaadb']]`
- ブロック [`00acaadc`](#insn-00acaadc) 範囲 `[['00acaadc', '00acaaeb']]`

## 命令位置別の参照

- [`00acaa4c`](#insn-00acaa4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa50`](#insn-00acaa50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa54`](#insn-00acaa54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa64`](#insn-00acaa64) → [`00acaa6c`](#insn-00acaa6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa70`](#insn-00acaa70) → [`00acaac4`](#insn-00acaac4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa80`](#insn-00acaa80) → [`00acaa98`](#insn-00acaa98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa88`](#insn-00acaa88) → [`00acaaa8`](#insn-00acaaa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa90`](#insn-00acaa90) → [`00acaab8`](#insn-00acaab8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa94`](#insn-00acaa94) → [`00acaa68`](#insn-00acaa68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaa9c`](#insn-00acaa9c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acaaa4`](#insn-00acaaa4) → [`00acaa8c`](#insn-00acaa8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaaac`](#insn-00acaaac) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acaab4`](#insn-00acaab4) → [`00acaa68`](#insn-00acaa68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaabc`](#insn-00acaabc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acaac0`](#insn-00acaac0) → [`00acaa68`](#insn-00acaa68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaac8`](#insn-00acaac8) → [`00acaadc`](#insn-00acaadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaacc`](#insn-00acaacc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaad0`](#insn-00acaad0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaad4`](#insn-00acaad4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaad8`](#insn-00acaad8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acaadc`](#insn-00acaadc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaae0`](#insn-00acaae0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaae4`](#insn-00acaae4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acaa4c`](#insn-00acaa4c)

~~~json
{
  "source": "00acaa4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa50`](#insn-00acaa50)

~~~json
{
  "source": "00acaa50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa54`](#insn-00acaa54)

~~~json
{
  "source": "00acaa54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa64`](#insn-00acaa64)

~~~json
{
  "source": "00acaa64",
  "target": "00acaa6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa70`](#insn-00acaa70)

~~~json
{
  "source": "00acaa70",
  "target": "00acaac4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa80`](#insn-00acaa80)

~~~json
{
  "source": "00acaa80",
  "target": "00acaa98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa88`](#insn-00acaa88)

~~~json
{
  "source": "00acaa88",
  "target": "00acaaa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa90`](#insn-00acaa90)

~~~json
{
  "source": "00acaa90",
  "target": "00acaab8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa94`](#insn-00acaa94)

~~~json
{
  "source": "00acaa94",
  "target": "00acaa68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaa9c`](#insn-00acaa9c)

~~~json
{
  "source": "00acaa9c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaaa4`](#insn-00acaaa4)

~~~json
{
  "source": "00acaaa4",
  "target": "00acaa8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaaac`](#insn-00acaaac)

~~~json
{
  "source": "00acaaac",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaab4`](#insn-00acaab4)

~~~json
{
  "source": "00acaab4",
  "target": "00acaa68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaabc`](#insn-00acaabc)

~~~json
{
  "source": "00acaabc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaac0`](#insn-00acaac0)

~~~json
{
  "source": "00acaac0",
  "target": "00acaa68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaac8`](#insn-00acaac8)

~~~json
{
  "source": "00acaac8",
  "target": "00acaadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaacc`](#insn-00acaacc)

~~~json
{
  "source": "00acaacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaad0`](#insn-00acaad0)

~~~json
{
  "source": "00acaad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaad4`](#insn-00acaad4)

~~~json
{
  "source": "00acaad4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaad8`](#insn-00acaad8)

~~~json
{
  "source": "00acaad8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaadc`](#insn-00acaadc)

~~~json
{
  "source": "00acaadc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaae0`](#insn-00acaae0)

~~~json
{
  "source": "00acaae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaae4`](#insn-00acaae4)

~~~json
{
  "source": "00acaae4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
