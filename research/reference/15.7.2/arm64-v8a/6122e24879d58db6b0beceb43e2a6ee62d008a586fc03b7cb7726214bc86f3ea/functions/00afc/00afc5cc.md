# 00afc5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afc694`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc694.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-6e4a5f06e4fafe685538ecb4642f91f2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc5cc",
  "name": "_ZN8firebase15CleanupNotifier10CleanupAllEv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08bd96baf28270f855e2de42c684fe5f2f191fd9c0435da7659459d1a0b97362",
  "source_text_sha256": "08bd96baf28270f855e2de42c684fe5f2f191fd9c0435da7659459d1a0b97362",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afc5cc",
        "00afc63b"
      ]
    ],
    "bytes_sha256": "e33a8585bc2e38891847fad0beeeca6b64b61adec5bf707eca58f259ec5f6e1f",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bde810](../00bde/00bde810.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddcb0](../00bdd/00bddcb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 758 bytes

~~~c

void _ZN8firebase15CleanupNotifier10CleanupAllEv(long param_1)

{
  undefined8 uVar1;
  long lVar2;
  
  _ZN8firebase5Mutex7AcquireEv();
  if (*(char *)(param_1 + 0x40) == '\0') {
    lVar2 = *(long *)(param_1 + 0x28);
    while (lVar2 != param_1 + 0x30) {
                    /* try { // try from 00afc5fc to 00bfc60f has its CatchHandler @ 00b00398 */
      uVar1 = *(undefined8 *)(lVar2 + 0x20);
      (**(code **)(lVar2 + 0x28))(uVar1);
                    /* try { // try from 00afc610 to 00bfc61b has its CatchHandler @ 00b00418 */
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(param_1,uVar1);
      lVar2 = *(long *)(param_1 + 0x28);
    }
    *(undefined1 *)(param_1 + 0x40) = 1;
  }
  _ZN8firebase5Mutex7ReleaseEv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afc5cc"></a> `00afc5cc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afc5d0"></a> `00afc5d0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc5d4"></a> `00afc5d4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc5d8"></a> `00afc5d8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afc5dc"></a> `00afc5dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afc5e0"></a> `00afc5e0` | `50 85 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00afc5e4"></a> `00afc5e4` | `68 02 41 39` | ldrb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00afc5e8"></a> `00afc5e8` | `08 02 00 35` | cbnz w8,0x00afc628 | `CONDITIONAL_JUMP`
<a id="insn-00afc5ec"></a> `00afc5ec` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00afc5f0"></a> `00afc5f0` | `75 c2 00 91` | add x21,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00afc5f4"></a> `00afc5f4` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00afc5f8"></a> `00afc5f8` | `40 01 00 54` | b.eq 0x00afc620 | `CONDITIONAL_JUMP`
<a id="insn-00afc5fc"></a> `00afc5fc` | `14 21 42 a9` | ldp x20,x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afc600"></a> `00afc600` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afc604"></a> `00afc604` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afc608"></a> `00afc608` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afc60c"></a> `00afc60c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00afc610"></a> `00afc610` | `a8 85 03 94` | bl 0x00bddcb0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc614"></a> `00afc614` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00afc618"></a> `00afc618` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00afc61c"></a> `00afc61c` | `01 ff ff 54` | b.ne 0x00afc5fc | `CONDITIONAL_JUMP`
<a id="insn-00afc620"></a> `00afc620` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afc624"></a> `00afc624` | `68 02 01 39` | strb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00afc628"></a> `00afc628` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afc62c"></a> `00afc62c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc630"></a> `00afc630` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc634"></a> `00afc634` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afc638"></a> `00afc638` | `3e 85 03 14` | b 0x00bddb30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afc5cc`](#insn-00afc5cc) 範囲 `[['00afc5cc', '00afc5eb']]`
  - `CONDITIONAL_JUMP` [`00afc5e8`](#insn-00afc5e8) → [`00afc628`](#insn-00afc628)
  - `FALL_THROUGH` [`00afc5e8`](#insn-00afc5e8) → [`00afc5ec`](#insn-00afc5ec)
- ブロック [`00afc5ec`](#insn-00afc5ec) 範囲 `[['00afc5ec', '00afc5fb']]`
  - `CONDITIONAL_JUMP` [`00afc5f8`](#insn-00afc5f8) → [`00afc620`](#insn-00afc620)
  - `FALL_THROUGH` [`00afc5f8`](#insn-00afc5f8) → [`00afc5fc`](#insn-00afc5fc)
- ブロック [`00afc5fc`](#insn-00afc5fc) 範囲 `[['00afc5fc', '00afc60f']]`
  - `FALL_THROUGH` [`00afc60c`](#insn-00afc60c) → [`00afc610`](#insn-00afc610)
- ブロック [`00afc610`](#insn-00afc610) 範囲 `[['00afc610', '00afc61f']]`
  - `CONDITIONAL_JUMP` [`00afc61c`](#insn-00afc61c) → [`00afc5fc`](#insn-00afc5fc)
  - `FALL_THROUGH` [`00afc61c`](#insn-00afc61c) → [`00afc620`](#insn-00afc620)
- ブロック [`00afc620`](#insn-00afc620) 範囲 `[['00afc620', '00afc627']]`
  - `FALL_THROUGH` [`00afc624`](#insn-00afc624) → [`00afc628`](#insn-00afc628)
- ブロック [`00afc628`](#insn-00afc628) 範囲 `[['00afc628', '00afc63b']]`

## 命令位置別の参照

- [`00afc5cc`](#insn-00afc5cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5d0`](#insn-00afc5d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5d4`](#insn-00afc5d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5e0`](#insn-00afc5e0) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00afc5e8`](#insn-00afc5e8) → [`00afc628`](#insn-00afc628) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5f8`](#insn-00afc5f8) → [`00afc620`](#insn-00afc620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc610`](#insn-00afc610) → [`00bddcb0`](../00bdd/00bddcb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddcb0` · 推定シンボル `None` · 推定型 `None`
- [`00afc61c`](#insn-00afc61c) → [`00afc5fc`](#insn-00afc5fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc62c`](#insn-00afc62c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc630`](#insn-00afc630) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc638`](#insn-00afc638) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afc5cc`](#insn-00afc5cc)

~~~json
{
  "source": "00afc5cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5d0`](#insn-00afc5d0)

~~~json
{
  "source": "00afc5d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5d4`](#insn-00afc5d4)

~~~json
{
  "source": "00afc5d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5e0`](#insn-00afc5e0)

~~~json
{
  "source": "00afc5e0",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc5e8`](#insn-00afc5e8)

~~~json
{
  "source": "00afc5e8",
  "target": "00afc628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5f8`](#insn-00afc5f8)

~~~json
{
  "source": "00afc5f8",
  "target": "00afc620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc610`](#insn-00afc610)

~~~json
{
  "source": "00afc610",
  "target": "00bddcb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc61c`](#insn-00afc61c)

~~~json
{
  "source": "00afc61c",
  "target": "00afc5fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc62c`](#insn-00afc62c)

~~~json
{
  "source": "00afc62c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc630`](#insn-00afc630)

~~~json
{
  "source": "00afc630",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc638`](#insn-00afc638)

~~~json
{
  "source": "00afc638",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
