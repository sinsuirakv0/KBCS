# 00baba8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00babb54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babb54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-3dcb36380fe23df4afc62d3d41a52a74)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baba8c",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ab322ba6d65757ed0cb93138ab7d0fea5f9e18099ea862b68ff74af9d56fe00",
  "source_text_sha256": "9ab322ba6d65757ed0cb93138ab7d0fea5f9e18099ea862b68ff74af9d56fe00",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baba8c",
        "00babb2b"
      ]
    ],
    "bytes_sha256": "e0e2de8e84f38a93566fbafb59f5385ee1d2f6172e4051b7e8802b82b33305ee",
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

- [00be1480](../00be1/00be1480.md)
- [00be1a80](../00be1/00be1a80.md)
- [00be1a90](../00be1/00be1a90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 698 bytes

~~~c

ulong _ZNKSt6__ndk17codecvtIwc9mbstate_tE11do_encodingEv(long param_1)

{
  int iVar1;
  __locale_t p_Var2;
  ulong uVar3;
  size_t sVar4;
  
  p_Var2 = uselocale(*(__locale_t *)(param_1 + 0x10));
  iVar1 = mbtowc((wchar_t *)0x0,(char *)0x0,4);
  if (p_Var2 != (__locale_t)0x0) {
    uselocale(p_Var2);
  }
  if (iVar1 == 0) {
    if (*(__locale_t *)(param_1 + 0x10) == (__locale_t)0x0) {
      uVar3 = 1;
    }
    else {
      p_Var2 = uselocale(*(__locale_t *)(param_1 + 0x10));
      sVar4 = __ctype_get_mb_cur_max();
      if (p_Var2 != (__locale_t)0x0) {
        uselocale(p_Var2);
      }
      uVar3 = (ulong)(sVar4 == 1);
    }
  }
  else {
    uVar3 = 0xffffffff;
  }
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baba8c"></a> `00baba8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baba90"></a> `00baba90` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00baba94"></a> `00baba94` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baba98"></a> `00baba98` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baba9c"></a> `00baba9c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00babaa0"></a> `00babaa0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00babaa4"></a> `00babaa4` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00babaa8"></a> `00babaa8` | `76 d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00babaac"></a> `00babaac` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00babab0"></a> `00babab0` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00babab4"></a> `00babab4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00babab8"></a> `00babab8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bababc"></a> `00bababc` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00babac0"></a> `00babac0` | `f0 d7 00 94` | bl 0x00be1a80 | `UNCONDITIONAL_CALL`
<a id="insn-00babac4"></a> `00babac4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00babac8"></a> `00babac8` | `74 00 00 b4` | cbz x20,0x00babad4 | `CONDITIONAL_JUMP`
<a id="insn-00babacc"></a> `00babacc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00babad0"></a> `00babad0` | `6c d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00babad4"></a> `00babad4` | `75 00 00 34` | cbz w21,0x00babae0 | `CONDITIONAL_JUMP`
<a id="insn-00babad8"></a> `00babad8` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00babadc"></a> `00babadc` | `0f 00 00 14` | b 0x00babb18 | `UNCONDITIONAL_JUMP`
<a id="insn-00babae0"></a> `00babae0` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babae4"></a> `00babae4` | `80 01 00 b4` | cbz x0,0x00babb14 | `CONDITIONAL_JUMP`
<a id="insn-00babae8"></a> `00babae8` | `66 d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00babaec"></a> `00babaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00babaf0"></a> `00babaf0` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00babaf4"></a> `00babaf4` | `e7 d7 00 94` | bl 0x00be1a90 | `UNCONDITIONAL_CALL`
<a id="insn-00babaf8"></a> `00babaf8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00babafc"></a> `00babafc` | `73 00 00 b4` | cbz x19,0x00babb08 | `CONDITIONAL_JUMP`
<a id="insn-00babb00"></a> `00babb00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00babb04"></a> `00babb04` | `5f d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00babb08"></a> `00babb08` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00babb0c"></a> `00babb0c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00babb10"></a> `00babb10` | `02 00 00 14` | b 0x00babb18 | `UNCONDITIONAL_JUMP`
<a id="insn-00babb14"></a> `00babb14` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00babb18"></a> `00babb18` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babb1c"></a> `00babb1c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babb20"></a> `00babb20` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00babb24"></a> `00babb24` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00babb28"></a> `00babb28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baba8c`](#insn-00baba8c) 範囲 `[['00baba8c', '00babacb']]`
  - `CONDITIONAL_JUMP` [`00babac8`](#insn-00babac8) → [`00babad4`](#insn-00babad4)
  - `FALL_THROUGH` [`00babac8`](#insn-00babac8) → [`00babacc`](#insn-00babacc)
- ブロック [`00babacc`](#insn-00babacc) 範囲 `[['00babacc', '00babad3']]`
  - `FALL_THROUGH` [`00babad0`](#insn-00babad0) → [`00babad4`](#insn-00babad4)
- ブロック [`00babad4`](#insn-00babad4) 範囲 `[['00babad4', '00babad7']]`
  - `CONDITIONAL_JUMP` [`00babad4`](#insn-00babad4) → [`00babae0`](#insn-00babae0)
  - `FALL_THROUGH` [`00babad4`](#insn-00babad4) → [`00babad8`](#insn-00babad8)
- ブロック [`00babad8`](#insn-00babad8) 範囲 `[['00babad8', '00babadf']]`
  - `UNCONDITIONAL_JUMP` [`00babadc`](#insn-00babadc) → [`00babb18`](#insn-00babb18)
- ブロック [`00babae0`](#insn-00babae0) 範囲 `[['00babae0', '00babae7']]`
  - `CONDITIONAL_JUMP` [`00babae4`](#insn-00babae4) → [`00babb14`](#insn-00babb14)
  - `FALL_THROUGH` [`00babae4`](#insn-00babae4) → [`00babae8`](#insn-00babae8)
- ブロック [`00babae8`](#insn-00babae8) 範囲 `[['00babae8', '00babaff']]`
  - `CONDITIONAL_JUMP` [`00babafc`](#insn-00babafc) → [`00babb08`](#insn-00babb08)
  - `FALL_THROUGH` [`00babafc`](#insn-00babafc) → [`00babb00`](#insn-00babb00)
- ブロック [`00babb00`](#insn-00babb00) 範囲 `[['00babb00', '00babb07']]`
  - `FALL_THROUGH` [`00babb04`](#insn-00babb04) → [`00babb08`](#insn-00babb08)
- ブロック [`00babb08`](#insn-00babb08) 範囲 `[['00babb08', '00babb13']]`
  - `UNCONDITIONAL_JUMP` [`00babb10`](#insn-00babb10) → [`00babb18`](#insn-00babb18)
- ブロック [`00babb14`](#insn-00babb14) 範囲 `[['00babb14', '00babb17']]`
  - `FALL_THROUGH` [`00babb14`](#insn-00babb14) → [`00babb18`](#insn-00babb18)
- ブロック [`00babb18`](#insn-00babb18) 範囲 `[['00babb18', '00babb2b']]`

## 命令位置別の参照

- [`00baba90`](#insn-00baba90) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba94`](#insn-00baba94) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba98`](#insn-00baba98) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babaa8`](#insn-00babaa8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00babab0`](#insn-00babab0) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babac0`](#insn-00babac0) → [`00be1a80`](../00be1/00be1a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a80` · 推定シンボル `None` · 推定型 `None`
- [`00babac8`](#insn-00babac8) → [`00babad4`](#insn-00babad4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babad0`](#insn-00babad0) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00babad4`](#insn-00babad4) → [`00babae0`](#insn-00babae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babadc`](#insn-00babadc) → [`00babb18`](#insn-00babb18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babae4`](#insn-00babae4) → [`00babb14`](#insn-00babb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babae8`](#insn-00babae8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00babaf0`](#insn-00babaf0) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babaf4`](#insn-00babaf4) → [`00be1a90`](../00be1/00be1a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a90` · 推定シンボル `None` · 推定型 `None`
- [`00babafc`](#insn-00babafc) → [`00babb08`](#insn-00babb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb04`](#insn-00babb04) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00babb10`](#insn-00babb10) → [`00babb18`](#insn-00babb18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb18`](#insn-00babb18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb1c`](#insn-00babb1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb20`](#insn-00babb20) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baba90`](#insn-00baba90)

~~~json
{
  "source": "00baba90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba94`](#insn-00baba94)

~~~json
{
  "source": "00baba94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba98`](#insn-00baba98)

~~~json
{
  "source": "00baba98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babaa8`](#insn-00babaa8)

~~~json
{
  "source": "00babaa8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babab0`](#insn-00babab0)

~~~json
{
  "source": "00babab0",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babac0`](#insn-00babac0)

~~~json
{
  "source": "00babac0",
  "target": "00be1a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babac8`](#insn-00babac8)

~~~json
{
  "source": "00babac8",
  "target": "00babad4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babad0`](#insn-00babad0)

~~~json
{
  "source": "00babad0",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babad4`](#insn-00babad4)

~~~json
{
  "source": "00babad4",
  "target": "00babae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babadc`](#insn-00babadc)

~~~json
{
  "source": "00babadc",
  "target": "00babb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babae4`](#insn-00babae4)

~~~json
{
  "source": "00babae4",
  "target": "00babb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babae8`](#insn-00babae8)

~~~json
{
  "source": "00babae8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babaf0`](#insn-00babaf0)

~~~json
{
  "source": "00babaf0",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babaf4`](#insn-00babaf4)

~~~json
{
  "source": "00babaf4",
  "target": "00be1a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babafc`](#insn-00babafc)

~~~json
{
  "source": "00babafc",
  "target": "00babb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb04`](#insn-00babb04)

~~~json
{
  "source": "00babb04",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb10`](#insn-00babb10)

~~~json
{
  "source": "00babb10",
  "target": "00babb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb18`](#insn-00babb18)

~~~json
{
  "source": "00babb18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb1c`](#insn-00babb1c)

~~~json
{
  "source": "00babb1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb20`](#insn-00babb20)

~~~json
{
  "source": "00babb20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
