# 00baaffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bab0c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab0c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-12d085455fd75cd0011d39794b0a3678)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaffc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5ce9b6b7f60c7d13ae8ef74d181f690fca85bf61b872dbf43e6688bd2a43789",
  "source_text_sha256": "c5ce9b6b7f60c7d13ae8ef74d181f690fca85bf61b872dbf43e6688bd2a43789",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaffc",
        "00bab097"
      ]
    ],
    "bytes_sha256": "3869bd650b47917d5561f0b34b0b34b7aab1687932a0f754a98b00b6a1b489e9",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a00](../00be1/00be1a00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 566 bytes

~~~c

byte * _ZNKSt6__ndk112ctype_bynameIwE8do_widenEPKcS3_Pw
                 (long param_1,byte *param_2,byte *param_3,wint_t *param_4)

{
  byte bVar1;
  byte *pbVar2;
  wint_t wVar3;
  __locale_t __dataset;
  
  pbVar2 = param_2;
  for (; param_2 != param_3; param_2 = param_2 + 1) {
    bVar1 = *param_2;
    __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
    wVar3 = btowc((uint)bVar1);
    if (__dataset != (__locale_t)0x0) {
      uselocale(__dataset);
    }
    *param_4 = wVar3;
    pbVar2 = param_3;
    param_4 = param_4 + 1;
  }
  return pbVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaffc"></a> `00baaffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bab000"></a> `00bab000` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bab004"></a> `00bab004` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab008"></a> `00bab008` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab00c"></a> `00bab00c` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab010"></a> `00bab010` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab014"></a> `00bab014` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bab018"></a> `00bab018` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bab01c"></a> `00bab01c` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bab020"></a> `00bab020` | `c0 02 00 54` | b.eq 0x00bab078 | `CONDITIONAL_JUMP`
<a id="insn-00bab024"></a> `00bab024` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bab028"></a> `00bab028` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bab02c"></a> `00bab02c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bab030"></a> `00bab030` | `05 00 00 14` | b 0x00bab044 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab034"></a> `00bab034` | `73 06 00 91` | add x19,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00bab038"></a> `00bab038` | `b7 46 00 b8` | str w23,[x21], #0x4 | `FALL_THROUGH`
<a id="insn-00bab03c"></a> `00bab03c` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bab040"></a> `00bab040` | `a0 01 00 54` | b.eq 0x00bab074 | `CONDITIONAL_JUMP`
<a id="insn-00bab044"></a> `00bab044` | `c0 0a 40 f9` | ldr x0,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bab048"></a> `00bab048` | `77 02 40 39` | ldrb w23,[x19] | `FALL_THROUGH`
<a id="insn-00bab04c"></a> `00bab04c` | `0d d9 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00bab050"></a> `00bab050` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bab054"></a> `00bab054` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab058"></a> `00bab058` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00bab05c"></a> `00bab05c` | `69 da 00 94` | bl 0x00be1a00 | `UNCONDITIONAL_CALL`
<a id="insn-00bab060"></a> `00bab060` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bab064"></a> `00bab064` | `98 fe ff b4` | cbz x24,0x00bab034 | `CONDITIONAL_JUMP`
<a id="insn-00bab068"></a> `00bab068` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bab06c"></a> `00bab06c` | `05 d9 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00bab070"></a> `00bab070` | `f1 ff ff 17` | b 0x00bab034 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab074"></a> `00bab074` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00bab078"></a> `00bab078` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bab07c"></a> `00bab07c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab080"></a> `00bab080` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab084"></a> `00bab084` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab088"></a> `00bab088` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab08c"></a> `00bab08c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bab090"></a> `00bab090` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bab094"></a> `00bab094` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaffc`](#insn-00baaffc) 範囲 `[['00baaffc', '00bab023']]`
  - `CONDITIONAL_JUMP` [`00bab020`](#insn-00bab020) → [`00bab078`](#insn-00bab078)
  - `FALL_THROUGH` [`00bab020`](#insn-00bab020) → [`00bab024`](#insn-00bab024)
- ブロック [`00bab024`](#insn-00bab024) 範囲 `[['00bab024', '00bab033']]`
  - `UNCONDITIONAL_JUMP` [`00bab030`](#insn-00bab030) → [`00bab044`](#insn-00bab044)
- ブロック [`00bab034`](#insn-00bab034) 範囲 `[['00bab034', '00bab043']]`
  - `CONDITIONAL_JUMP` [`00bab040`](#insn-00bab040) → [`00bab074`](#insn-00bab074)
  - `FALL_THROUGH` [`00bab040`](#insn-00bab040) → [`00bab044`](#insn-00bab044)
- ブロック [`00bab044`](#insn-00bab044) 範囲 `[['00bab044', '00bab067']]`
  - `CONDITIONAL_JUMP` [`00bab064`](#insn-00bab064) → [`00bab034`](#insn-00bab034)
  - `FALL_THROUGH` [`00bab064`](#insn-00bab064) → [`00bab068`](#insn-00bab068)
- ブロック [`00bab068`](#insn-00bab068) 範囲 `[['00bab068', '00bab073']]`
  - `UNCONDITIONAL_JUMP` [`00bab070`](#insn-00bab070) → [`00bab034`](#insn-00bab034)
- ブロック [`00bab074`](#insn-00bab074) 範囲 `[['00bab074', '00bab077']]`
  - `FALL_THROUGH` [`00bab074`](#insn-00bab074) → [`00bab078`](#insn-00bab078)
- ブロック [`00bab078`](#insn-00bab078) 範囲 `[['00bab078', '00bab097']]`

## 命令位置別の参照

- [`00bab004`](#insn-00bab004) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab008`](#insn-00bab008) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab00c`](#insn-00bab00c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab010`](#insn-00bab010) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab020`](#insn-00bab020) → [`00bab078`](#insn-00bab078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab030`](#insn-00bab030) → [`00bab044`](#insn-00bab044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab040`](#insn-00bab040) → [`00bab074`](#insn-00bab074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab04c`](#insn-00bab04c) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00bab054`](#insn-00bab054) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab05c`](#insn-00bab05c) → [`00be1a00`](../00be1/00be1a00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a00` · 推定シンボル `None` · 推定型 `None`
- [`00bab064`](#insn-00bab064) → [`00bab034`](#insn-00bab034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab06c`](#insn-00bab06c) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00bab070`](#insn-00bab070) → [`00bab034`](#insn-00bab034) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab07c`](#insn-00bab07c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab080`](#insn-00bab080) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab084`](#insn-00bab084) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab088`](#insn-00bab088) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bab004`](#insn-00bab004)

~~~json
{
  "source": "00bab004",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab008`](#insn-00bab008)

~~~json
{
  "source": "00bab008",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab00c`](#insn-00bab00c)

~~~json
{
  "source": "00bab00c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab010`](#insn-00bab010)

~~~json
{
  "source": "00bab010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab020`](#insn-00bab020)

~~~json
{
  "source": "00bab020",
  "target": "00bab078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab030`](#insn-00bab030)

~~~json
{
  "source": "00bab030",
  "target": "00bab044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab040`](#insn-00bab040)

~~~json
{
  "source": "00bab040",
  "target": "00bab074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab04c`](#insn-00bab04c)

~~~json
{
  "source": "00bab04c",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab054`](#insn-00bab054)

~~~json
{
  "source": "00bab054",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab05c`](#insn-00bab05c)

~~~json
{
  "source": "00bab05c",
  "target": "00be1a00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab064`](#insn-00bab064)

~~~json
{
  "source": "00bab064",
  "target": "00bab034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab06c`](#insn-00bab06c)

~~~json
{
  "source": "00bab06c",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab070`](#insn-00bab070)

~~~json
{
  "source": "00bab070",
  "target": "00bab034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab07c`](#insn-00bab07c)

~~~json
{
  "source": "00bab07c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab080`](#insn-00bab080)

~~~json
{
  "source": "00bab080",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab084`](#insn-00bab084)

~~~json
{
  "source": "00bab084",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab088`](#insn-00bab088)

~~~json
{
  "source": "00bab088",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
