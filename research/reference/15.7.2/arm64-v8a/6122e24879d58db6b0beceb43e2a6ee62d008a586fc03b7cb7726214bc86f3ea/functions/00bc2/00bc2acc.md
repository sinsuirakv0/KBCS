# 00bc2acc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bc2b94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-29c510e6612c7b61d5bc23e5bb162b79)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc2acc",
  "name": "FUN_00bc2acc",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aad906b24b70131c181557393722972f1dabc903bc7805cb256538b2e8c52076",
  "source_text_sha256": "aad906b24b70131c181557393722972f1dabc903bc7805cb256538b2e8c52076",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc2acc",
        "00bc2b77"
      ]
    ],
    "bytes_sha256": "28b578df4c7554dfc7d879a52fa58ddc3a4ff192d7872952ad8c4784d9d6a77b",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbdd50](../00bbd/00bbdd50.md)
- [00bc1bc0](../00bc1/00bc1bc0.md)

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1104 bytes

~~~c

undefined8 * FUN_00bc2acc(long param_1,char *param_2)

{
  undefined8 *puVar1;
  size_t sVar2;
  long lVar3;
  undefined8 *puVar4;
  void *pvVar5;
  
  pvVar5 = *(void **)(param_1 + 0x1330);
  lVar3 = *(long *)((long)pvVar5 + 8);
  puVar1 = pvVar5;
  if (lVar3 - 0xfd0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar1 = pvVar5;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar3 + 0x20;
  sVar2 = strlen(param_2);
  puVar4 = (undefined8 *)((long)puVar1 + lVar3 + 0x10);
  *puVar4 = &PTR_FUN_00c17798;
                    /* try { // try from 00bc2b40 to 00cc2b47 has its CatchHandler @ 00bc87cc */
  *(undefined1 *)((long)puVar1 + lVar3 + 0x18) = 8;
  *(char **)((long)puVar1 + lVar3 + 0x20) = param_2;
  *(size_t *)((long)puVar1 + lVar3 + 0x28) = sVar2;
  *(ushort *)((long)puVar1 + lVar3 + 0x19) =
       *(ushort *)((long)puVar1 + lVar3 + 0x19) & 0xf000 | 0x540;
  return puVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc2acc"></a> `00bc2acc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bc2ad0"></a> `00bc2ad0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bc2ad4"></a> `00bc2ad4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2ad8"></a> `00bc2ad8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2adc"></a> `00bc2adc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bc2ae0"></a> `00bc2ae0` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc2ae4"></a> `00bc2ae4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bc2ae8"></a> `00bc2ae8` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bc2aec"></a> `00bc2aec` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bc2af0"></a> `00bc2af0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bc2af4"></a> `00bc2af4` | `28 01 00 54` | b.hi 0x00bc2b18 | `CONDITIONAL_JUMP`
<a id="insn-00bc2af8"></a> `00bc2af8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bc2afc"></a> `00bc2afc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bc2b00"></a> `00bc2b00` | `74 69 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2b04"></a> `00bc2b04` | `80 03 00 b4` | cbz x0,0x00bc2b74 | `CONDITIONAL_JUMP`
<a id="insn-00bc2b08"></a> `00bc2b08` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bc2b0c"></a> `00bc2b0c` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bc2b10"></a> `00bc2b10` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc2b14"></a> `00bc2b14` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc2b18"></a> `00bc2b18` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bc2b1c"></a> `00bc2b1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc2b20"></a> `00bc2b20` | `b4 02 08 8b` | add x20,x21,x8 | `FALL_THROUGH`
<a id="insn-00bc2b24"></a> `00bc2b24` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bc2b28"></a> `00bc2b28` | `5a 61 00 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2b2c"></a> `00bc2b2c` | `a9 02 00 b0` | adrp x9,0xc17000 | `FALL_THROUGH`
<a id="insn-00bc2b30"></a> `00bc2b30` | `29 61 1e 91` | add x9,x9,#0x798 | `FALL_THROUGH`
<a id="insn-00bc2b34"></a> `00bc2b34` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00bc2b38"></a> `00bc2b38` | `89 0e 01 f8` | str x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00bc2b3c"></a> `00bc2b3c` | `89 92 40 78` | ldurh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bc2b40"></a> `00bc2b40` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc2b44"></a> `00bc2b44` | `0a 01 80 52` | mov w10,#0x8 | `FALL_THROUGH`
<a id="insn-00bc2b48"></a> `00bc2b48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc2b4c"></a> `00bc2b4c` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bc2b50"></a> `00bc2b50` | `8a 22 00 39` | strb w10,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bc2b54"></a> `00bc2b54` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00bc2b58"></a> `00bc2b58` | `93 22 01 a9` | stp x19,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2b5c"></a> `00bc2b5c` | `89 92 00 78` | sturh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bc2b60"></a> `00bc2b60` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2b64"></a> `00bc2b64` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2b68"></a> `00bc2b68` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bc2b6c"></a> `00bc2b6c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc2b70"></a> `00bc2b70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc2b74"></a> `00bc2b74` | `57 61 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc2acc`](#insn-00bc2acc) 範囲 `[['00bc2acc', '00bc2af7']]`
  - `CONDITIONAL_JUMP` [`00bc2af4`](#insn-00bc2af4) → [`00bc2b18`](#insn-00bc2b18)
  - `FALL_THROUGH` [`00bc2af4`](#insn-00bc2af4) → [`00bc2af8`](#insn-00bc2af8)
- ブロック [`00bc2af8`](#insn-00bc2af8) 範囲 `[['00bc2af8', '00bc2b07']]`
  - `CONDITIONAL_JUMP` [`00bc2b04`](#insn-00bc2b04) → [`00bc2b74`](#insn-00bc2b74)
  - `FALL_THROUGH` [`00bc2b04`](#insn-00bc2b04) → [`00bc2b08`](#insn-00bc2b08)
- ブロック [`00bc2b08`](#insn-00bc2b08) 範囲 `[['00bc2b08', '00bc2b17']]`
  - `FALL_THROUGH` [`00bc2b14`](#insn-00bc2b14) → [`00bc2b18`](#insn-00bc2b18)
- ブロック [`00bc2b18`](#insn-00bc2b18) 範囲 `[['00bc2b18', '00bc2b3f']]`
  - `FALL_THROUGH` [`00bc2b3c`](#insn-00bc2b3c) → [`00bc2b40`](#insn-00bc2b40)
- ブロック [`00bc2b40`](#insn-00bc2b40) 範囲 `[['00bc2b40', '00bc2b73']]`
- ブロック [`00bc2b74`](#insn-00bc2b74) 範囲 `[['00bc2b74', '00bc2b77']]`

## 命令位置別の参照

- [`00bc2ad0`](#insn-00bc2ad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2ad4`](#insn-00bc2ad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2ad8`](#insn-00bc2ad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2af4`](#insn-00bc2af4) → [`00bc2b18`](#insn-00bc2b18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b00`](#insn-00bc2b00) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b04`](#insn-00bc2b04) → [`00bc2b74`](#insn-00bc2b74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b28`](#insn-00bc2b28) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b38`](#insn-00bc2b38) → `00c17798`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc2b60`](#insn-00bc2b60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b64`](#insn-00bc2b64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b68`](#insn-00bc2b68) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b74`](#insn-00bc2b74) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc2ad0`](#insn-00bc2ad0)

~~~json
{
  "source": "00bc2ad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2ad4`](#insn-00bc2ad4)

~~~json
{
  "source": "00bc2ad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2ad8`](#insn-00bc2ad8)

~~~json
{
  "source": "00bc2ad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2af4`](#insn-00bc2af4)

~~~json
{
  "source": "00bc2af4",
  "target": "00bc2b18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b00`](#insn-00bc2b00)

~~~json
{
  "source": "00bc2b00",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2b04`](#insn-00bc2b04)

~~~json
{
  "source": "00bc2b04",
  "target": "00bc2b74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b28`](#insn-00bc2b28)

~~~json
{
  "source": "00bc2b28",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2b38`](#insn-00bc2b38)

~~~json
{
  "source": "00bc2b38",
  "target": "00c17798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17798",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc2b60`](#insn-00bc2b60)

~~~json
{
  "source": "00bc2b60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b64`](#insn-00bc2b64)

~~~json
{
  "source": "00bc2b64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b68`](#insn-00bc2b68)

~~~json
{
  "source": "00bc2b68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b74`](#insn-00bc2b74)

~~~json
{
  "source": "00bc2b74",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
