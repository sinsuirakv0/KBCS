# 00bd3efc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd3fc4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3fc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-d0fb38db6fbdb4044bbf3f04c7c40664)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd3efc",
  "name": "FUN_00bd3efc",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6633314ed5dfdaa2f771f347251c9db3c0530bf7ca14b25ebc54a33c36460d17",
  "source_text_sha256": "6633314ed5dfdaa2f771f347251c9db3c0530bf7ca14b25ebc54a33c36460d17",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd3efc",
        "00bd3faf"
      ]
    ],
    "bytes_sha256": "914377287ec4c6ec0edbbea93e3f27b66c3617eb2484228f3b42e7aac408c9c7",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbdd50](../00bbd/00bbdd50.md)

## 呼び出し先

- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1071 bytes

~~~c

void FUN_00bd3efc(long param_1,undefined8 *param_2,long *param_3)

{
  ushort uVar1;
  undefined8 *puVar2;
  long lVar3;
  long lVar4;
  undefined8 uVar5;
  void *pvVar6;
  
  pvVar6 = *(void **)(param_1 + 0x1330);
  lVar3 = *(long *)((long)pvVar6 + 8);
  puVar2 = pvVar6;
  if (lVar3 - 0xfd0U < 0xfffffffffffff010) {
    puVar2 = malloc(0x1000);
    if (puVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar2 = pvVar6;
    puVar2[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar2;
  }
  lVar4 = *param_3;
  *(long *)((long)puVar2 + 8) = lVar3 + 0x20;
  uVar1 = *(ushort *)(lVar4 + 9);
  *(undefined ***)((long)puVar2 + lVar3 + 0x10) = &PTR_FUN_00c19f58;
  uVar5 = *param_2;
  *(undefined1 *)((long)puVar2 + lVar3 + 0x18) = 0xe;
  *(ushort *)((long)puVar2 + lVar3 + 0x19) =
       uVar1 & 0xc0 | 0x500 | *(ushort *)((long)puVar2 + lVar3 + 0x19) & 0xf000;
  *(undefined8 *)((long)puVar2 + lVar3 + 0x20) = uVar5;
  *(long *)((long)puVar2 + lVar3 + 0x28) = lVar4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd3efc"></a> `00bd3efc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd3f00"></a> `00bd3f00` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd3f04"></a> `00bd3f04` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3f08"></a> `00bd3f08` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3f0c"></a> `00bd3f0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd3f10"></a> `00bd3f10` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd3f14"></a> `00bd3f14` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bd3f18"></a> `00bd3f18` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd3f1c"></a> `00bd3f1c` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3f20"></a> `00bd3f20` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bd3f24"></a> `00bd3f24` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bd3f28"></a> `00bd3f28` | `28 01 00 54` | b.hi 0x00bd3f4c | `CONDITIONAL_JUMP`
<a id="insn-00bd3f2c"></a> `00bd3f2c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd3f30"></a> `00bd3f30` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bd3f34"></a> `00bd3f34` | `67 24 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3f38"></a> `00bd3f38` | `a0 03 00 b4` | cbz x0,0x00bd3fac | `CONDITIONAL_JUMP`
<a id="insn-00bd3f3c"></a> `00bd3f3c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bd3f40"></a> `00bd3f40` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bd3f44"></a> `00bd3f44` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd3f48"></a> `00bd3f48` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd3f4c"></a> `00bd3f4c` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bd3f50"></a> `00bd3f50` | `8a 02 40 f9` | ldr x10,[x20] | `FALL_THROUGH`
<a id="insn-00bd3f54"></a> `00bd3f54` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00bd3f58"></a> `00bd3f58` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3f5c"></a> `00bd3f5c` | `28 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bd3f60"></a> `00bd3f60` | `08 61 3d 91` | add x8,x8,#0xf58 | `FALL_THROUGH`
<a id="insn-00bd3f64"></a> `00bd3f64` | `49 91 40 78` | ldurh w9,[x10, #0x9] | `FALL_THROUGH`
<a id="insn-00bd3f68"></a> `00bd3f68` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bd3f6c"></a> `00bd3f6c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bd3f70"></a> `00bd3f70` | `0b a0 80 52` | mov w11,#0x500 | `FALL_THROUGH`
<a id="insn-00bd3f74"></a> `00bd3f74` | `6c 02 40 f9` | ldr x12,[x19] | `FALL_THROUGH`
<a id="insn-00bd3f78"></a> `00bd3f78` | `29 05 1a 12` | and w9,w9,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd3f7c"></a> `00bd3f7c` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00bd3f80"></a> `00bd3f80` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bd3f84"></a> `00bd3f84` | `cb 01 80 52` | mov w11,#0xe | `FALL_THROUGH`
<a id="insn-00bd3f88"></a> `00bd3f88` | `28 01 08 2a` | orr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00bd3f8c"></a> `00bd3f8c` | `0b 20 00 39` | strb w11,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3f90"></a> `00bd3f90` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bd3f94"></a> `00bd3f94` | `0c 28 01 a9` | stp x12,x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3f98"></a> `00bd3f98` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3f9c"></a> `00bd3f9c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3fa0"></a> `00bd3fa0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd3fa4"></a> `00bd3fa4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd3fa8"></a> `00bd3fa8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd3fac"></a> `00bd3fac` | `49 1c 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd3efc`](#insn-00bd3efc) 範囲 `[['00bd3efc', '00bd3f2b']]`
  - `CONDITIONAL_JUMP` [`00bd3f28`](#insn-00bd3f28) → [`00bd3f4c`](#insn-00bd3f4c)
  - `FALL_THROUGH` [`00bd3f28`](#insn-00bd3f28) → [`00bd3f2c`](#insn-00bd3f2c)
- ブロック [`00bd3f2c`](#insn-00bd3f2c) 範囲 `[['00bd3f2c', '00bd3f3b']]`
  - `CONDITIONAL_JUMP` [`00bd3f38`](#insn-00bd3f38) → [`00bd3fac`](#insn-00bd3fac)
  - `FALL_THROUGH` [`00bd3f38`](#insn-00bd3f38) → [`00bd3f3c`](#insn-00bd3f3c)
- ブロック [`00bd3f3c`](#insn-00bd3f3c) 範囲 `[['00bd3f3c', '00bd3f4b']]`
  - `FALL_THROUGH` [`00bd3f48`](#insn-00bd3f48) → [`00bd3f4c`](#insn-00bd3f4c)
- ブロック [`00bd3f4c`](#insn-00bd3f4c) 範囲 `[['00bd3f4c', '00bd3fab']]`
- ブロック [`00bd3fac`](#insn-00bd3fac) 範囲 `[['00bd3fac', '00bd3faf']]`

## 命令位置別の参照

- [`00bd3f00`](#insn-00bd3f00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f04`](#insn-00bd3f04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f08`](#insn-00bd3f08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f28`](#insn-00bd3f28) → [`00bd3f4c`](#insn-00bd3f4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f34`](#insn-00bd3f34) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f38`](#insn-00bd3f38) → [`00bd3fac`](#insn-00bd3fac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f68`](#insn-00bd3f68) → `00c19f58`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bd3f98`](#insn-00bd3f98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f9c`](#insn-00bd3f9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3fa0`](#insn-00bd3fa0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3fac`](#insn-00bd3fac) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd3f00`](#insn-00bd3f00)

~~~json
{
  "source": "00bd3f00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f04`](#insn-00bd3f04)

~~~json
{
  "source": "00bd3f04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f08`](#insn-00bd3f08)

~~~json
{
  "source": "00bd3f08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f28`](#insn-00bd3f28)

~~~json
{
  "source": "00bd3f28",
  "target": "00bd3f4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f34`](#insn-00bd3f34)

~~~json
{
  "source": "00bd3f34",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3f38`](#insn-00bd3f38)

~~~json
{
  "source": "00bd3f38",
  "target": "00bd3fac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f68`](#insn-00bd3f68)

~~~json
{
  "source": "00bd3f68",
  "target": "00c19f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd3f98`](#insn-00bd3f98)

~~~json
{
  "source": "00bd3f98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f9c`](#insn-00bd3f9c)

~~~json
{
  "source": "00bd3f9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3fa0`](#insn-00bd3fa0)

~~~json
{
  "source": "00bd3fa0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3fac`](#insn-00bd3fac)

~~~json
{
  "source": "00bd3fac",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
